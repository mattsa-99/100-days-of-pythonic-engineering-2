"""Day 04: detect and fix data skew in Spark joins.

Fixes are ordered from least to most effort:
1. Filter null join keys.
2. Enable AQE skew join handling.
3. Broadcast the small side (see Day 03).
4. Salt the hot key.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def top_keys(df: DataFrame, key: str, limit: int = 10) -> DataFrame:
    """Return the most frequent values of a join key, to spot hot keys.

    Args:
        df: DataFrame to inspect.
        key: Name of the join key column.
        limit: Number of top keys to return.

    Returns:
        DataFrame with columns ``key`` and ``count``, sorted by count descending.
    """
    return df.groupBy(key).count().orderBy(F.desc("count")).limit(limit)


def enable_aqe_skew_join(spark: SparkSession) -> None:
    """Turn on Adaptive Query Execution and its skew join optimization.

    Args:
        spark: Active Spark session. Its configuration is updated in place.
    """
    spark.conf.set("spark.sql.adaptive.enabled", "true")
    spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")


def drop_null_keys(df: DataFrame, key: str) -> DataFrame:
    """Remove rows whose join key is null before joining.

    Null keys never match in an inner join, but they still land in a single
    shuffle partition and can create a huge straggler task.

    Args:
        df: Input DataFrame.
        key: Name of the join key column.

    Returns:
        DataFrame without null keys.
    """
    return df.filter(F.col(key).isNotNull())


def salted_join(
    big: DataFrame,
    small: DataFrame,
    key: str,
    n_salts: int = 8,
    how: str = "inner",
) -> DataFrame:
    """Join two DataFrames splitting each hot key into ``n_salts`` buckets.

    The big side gets a random salt in ``[0, n_salts)``. The small side is
    replicated once per salt value, so every salted row still finds its match.

    Args:
        big: Large, skewed DataFrame.
        small: Smaller DataFrame (replicated ``n_salts`` times).
        key: Name of the join key column, present in both DataFrames.
        n_salts: Number of buckets per key. Size it to the hot key volume.
        how: Join type. Must keep the big side (``inner`` or ``left``).

    Returns:
        Joined DataFrame without the helper ``salt`` column.
    """
    big_salted = big.withColumn("salt", (F.rand() * n_salts).cast("int"))
    small_salted = small.withColumn(
        "salt", F.explode(F.array(*[F.lit(i) for i in range(n_salts)]))
    )
    return big_salted.join(small_salted, [key, "salt"], how).drop("salt")


if __name__ == "__main__":
    spark = SparkSession.builder.appName("day04-data-skew").getOrCreate()
    enable_aqe_skew_join(spark)

    # 90% of the rows share the same customer_id: a classic hot key.
    orders = spark.range(1_000_000).withColumn(
        "customer_id",
        F.when(F.rand() < 0.9, F.lit(1)).otherwise((F.rand() * 1000).cast("int")),
    )
    customers = spark.range(1000).withColumnRenamed("id", "customer_id")

    top_keys(orders, "customer_id").show()
    result = salted_join(drop_null_keys(orders, "customer_id"), customers, "customer_id")
    print(result.count())
