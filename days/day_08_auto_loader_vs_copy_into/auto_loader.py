"""Day 08: Auto Loader ingestion into Bronze, run as an incremental batch."""

from pyspark.sql import SparkSession
from pyspark.sql.streaming import StreamingQuery


def ingest_with_auto_loader(
    spark: SparkSession,
    source_path: str,
    table: str,
    schema_path: str,
    checkpoint_path: str,
    file_format: str = "json",
) -> StreamingQuery:
    """Load only new files from cloud storage into a Delta table.

    ``trigger(availableNow=True)`` processes everything pending and stops,
    so no cluster has to stay on 24/7.

    Args:
        spark: Active Spark session.
        source_path: Folder with landing files (e.g. an ``abfss://`` path).
        table: Target Bronze table.
        schema_path: Location where Auto Loader stores the inferred schema.
        checkpoint_path: Location that tracks which files were processed.
        file_format: Format of the source files.

    Returns:
        The running streaming query. Call ``awaitTermination()`` to block.
    """
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", file_format)
        .option("cloudFiles.schemaLocation", schema_path)
        .load(source_path)
        .writeStream.option("checkpointLocation", checkpoint_path)
        .trigger(availableNow=True)
        .toTable(table)
    )


# COPY INTO equivalent (fine for thousands of files or one-off loads):
COPY_INTO_SQL = """
COPY INTO bronze.orders
FROM 'abfss://raw@<account>.dfs.core.windows.net/orders/'
FILEFORMAT = JSON
COPY_OPTIONS ('mergeSchema' = 'true')
"""
