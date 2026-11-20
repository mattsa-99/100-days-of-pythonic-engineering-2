"""Day 05: repartition() vs coalesce()."""

from pyspark.sql import DataFrame, SparkSession
import pyspark.sql.functions as F


def partition_sizes(df: DataFrame) -> list[int]:
    """Count rows per partition to see how balanced a DataFrame is.

    Args:
        df: DataFrame to inspect.

    Returns:
        Row count of each partition, in partition order.
    """
    return (
        df.withColumn("partition_id", F.spark_partition_id())
        .groupBy("partition_id")
        .count()
        .orderBy("partition_id")
        .rdd.map(lambda row: row["count"])
        .collect()
    )


def write_compact(df: DataFrame, path: str, n_files: int) -> None:
    """Reduce the number of output files right before writing.

    ``coalesce`` merges neighbor partitions without a full shuffle, which is
    the cheap option at the end of a pipeline. Avoid ``coalesce(1)`` on large
    data: the whole write goes through a single task.

    Args:
        df: DataFrame to write.
        path: Target path.
        n_files: Desired number of output files.
    """
    df.coalesce(n_files).write.mode("overwrite").parquet(path)


if __name__ == "__main__":
    spark = SparkSession.builder.appName("day05-repartition").getOrCreate()
    df = spark.range(1_000_000).filter(F.col("id") % 7 != 0)

    print("repartition(8):", partition_sizes(df.repartition(8)))  # full shuffle, even
    print("coalesce(2):  ", partition_sizes(df.coalesce(2)))  # no full shuffle
    print("by column:    ", df.repartition(4, "id").rdd.getNumPartitions())
