"""Day 11: five data quality checks before promoting data to Silver.

All row-level checks run in a single aggregation (one Spark action) instead
of one ``.count()`` per check.
"""

from datetime import date

from pyspark.sql import DataFrame
import pyspark.sql.functions as F


class DataQualityError(ValueError):
    """Raised when at least one data quality check fails."""


def compute_checks(df: DataFrame, key: str, amount_col: str, date_col: str) -> dict[str, int]:
    """Compute failure counts for the row-level checks in one pass.

    Args:
        df: Candidate DataFrame for Silver.
        key: Primary/business key column.
        amount_col: Numeric column that must not be negative.
        date_col: Date column that must not be in the future.

    Returns:
        Mapping of check name to number of offending rows, plus ``row_count``
        and ``max_date`` helpers (as ordinal days) for freshness and volume.
    """
    row = df.agg(
        F.count(F.lit(1)).alias("row_count"),
        F.sum(F.col(key).isNull().cast("int")).alias("null_keys"),
        (F.count(F.col(key)) - F.countDistinct(key)).alias("duplicates"),
        F.sum((F.col(amount_col) < 0).cast("int")).alias("negative_amounts"),
        F.sum((F.col(date_col) > F.current_date()).cast("int")).alias("future_dates"),
        F.max(date_col).alias("max_date"),
    ).first()
    checks = {name: int(row[name] or 0) for name in row.asDict() if name != "max_date"}
    checks["max_date"] = row["max_date"].toordinal() if row["max_date"] else 0
    return checks


def validate(
    df: DataFrame,
    key: str,
    amount_col: str,
    date_col: str,
    expected_rows: int,
    tolerance: float = 0.5,
) -> None:
    """Run the five checks and raise if any fails.

    Args:
        df: Candidate DataFrame for Silver.
        key: Primary/business key column.
        amount_col: Numeric column that must not be negative.
        date_col: Date column used for range and freshness checks.
        expected_rows: Typical daily volume (e.g. average of the last 7 loads).
        tolerance: Allowed relative deviation from ``expected_rows``.

    Raises:
        DataQualityError: With the name and value of every failed check.
    """
    checks = compute_checks(df, key, amount_col, date_col)
    failed = {
        name: checks[name]
        for name in ("null_keys", "duplicates", "negative_amounts", "future_dates")
        if checks[name] > 0
    }
    if checks["max_date"] < date.today().toordinal():
        failed["stale_data"] = checks["max_date"]
    if abs(checks["row_count"] - expected_rows) > expected_rows * tolerance:
        failed["unexpected_volume"] = checks["row_count"]
    if failed:
        raise DataQualityError(f"Data quality checks failed: {failed}")
