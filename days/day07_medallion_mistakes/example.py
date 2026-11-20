"""Day 07: Bronze is raw and append-only, plus ingestion metadata (mistakes 1 and 5)."""

from pyspark.sql import DataFrame
import pyspark.sql.functions as F


def add_ingestion_metadata(df: DataFrame) -> DataFrame:
    """Add lineage columns to raw data without transforming business columns.

    Args:
        df: Raw DataFrame read from files (no cleaning applied).

    Returns:
        Same DataFrame plus ``_ingested_at`` and ``_source_file`` columns.
    """
    return df.withColumn("_ingested_at", F.current_timestamp()).withColumn(
        "_source_file", F.col("_metadata.file_path")
    )


def write_bronze(df: DataFrame, table: str) -> None:
    """Append raw data to a Bronze table. Never overwrite, never clean here.

    Args:
        df: Raw DataFrame with ingestion metadata.
        table: Fully qualified Bronze table name.
    """
    df.write.mode("append").saveAsTable(table)
