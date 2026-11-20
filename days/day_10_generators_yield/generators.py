"""Day 10: process huge files with generators instead of loading them into RAM."""

import csv
import sys
import tempfile
import tracemalloc
from collections.abc import Iterable, Iterator
from pathlib import Path


def read_all(path: Path) -> list[str]:
    """Load every line into memory at once (the anti-pattern).

    Args:
        path: File to read.

    Returns:
        All lines of the file.
    """
    with path.open(encoding="utf-8") as f:
        return f.readlines()


def read_rows(path: Path) -> Iterator[str]:
    """Yield the file one line at a time with constant memory.

    Args:
        path: File to read.

    Returns:
        Iterator over the lines of the file.
    """
    with path.open(encoding="utf-8") as f:
        yield from f


def parse_amounts(lines: Iterable[str]) -> Iterator[float]:
    """Lazily parse the ``amount`` column of CSV lines, skipping the header.

    Args:
        lines: CSV lines with ``id,amount`` columns, header included.

    Returns:
        Iterator over the parsed amounts.
    """
    reader = csv.DictReader(lines)
    for row in reader:
        yield float(row["amount"])


def peak_memory_mb(func_name: str, path: Path) -> float:
    """Measure peak Python memory while summing amounts with one strategy.

    Args:
        func_name: ``"read_all"`` or ``"read_rows"``.
        path: CSV file to process.

    Returns:
        Peak traced memory in megabytes.
    """
    reader = read_all if func_name == "read_all" else read_rows
    tracemalloc.start()
    sum(parse_amounts(reader(path)))
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / 1_000_000


def write_sample(path: Path, n_rows: int) -> None:
    """Write a sample CSV with ``id,amount`` columns.

    Args:
        path: Target file.
        n_rows: Number of data rows.
    """
    with path.open("w", encoding="utf-8") as f:
        f.write("id,amount\n")
        f.writelines(f"{i},{i % 100}.5\n" for i in range(n_rows))


if __name__ == "__main__":
    rows = int(sys.argv[1]) if len(sys.argv) > 1 else 500_000
    with tempfile.TemporaryDirectory() as tmp:
        sample = Path(tmp) / "big.csv"
        write_sample(sample, rows)
        for strategy in ("read_all", "read_rows"):
            print(f"{strategy:>9}: {peak_memory_mb(strategy, sample):8.2f} MB peak")
