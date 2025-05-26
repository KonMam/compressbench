from pathlib import Path
from typing import List

import typer

from compressbench import __version__
from compressbench.benchmark import run_benchmarks
from compressbench.compressors.gzip import GzipCompressor
from compressbench.compressors.lz4 import Lz4Compressor
from compressbench.compressors.snappy import SnappyCompressor
from compressbench.compressors.zstd import ZstdCompressor
from compressbench.results import output_results

app = typer.Typer(
    help="Benchmark compression algorithms on Parquet datasets.",
)

ALGORITHM_MAP = {"gzip": GzipCompressor, "snappy": SnappyCompressor, "lz4": Lz4Compressor, "zstd": ZstdCompressor}


@app.command()
def benchmark(
    input_file: str = typer.Argument(..., help="Path to the Parquet file to benchmark."),
    algorithms: list[str] = typer.Option(
        None,
        "--algorithms",
        "-a",
        help="Compression algorithms to test (gzip, snappy, lz4, zstd).",
    ),
    output_format: str = typer.Option("text", "--output-format", "-o", help="Output format: text, json, csv."),
    zstd_levels: List[int] = typer.Option(
        None,
        "--zstd-level",
        help="Zstandard compression levels to benchmark (e.g., --zstd-level 1 --zstd-level 3 --zstd-level 9).",
    ),
):
    """
    Run compression benchmark on the specified Parquet file.
    """
    if not Path(input_file).exists():
        typer.echo("Error: Input file does not exist.")
        raise typer.Exit(code=1)

    if not algorithms:
        algorithms = ["gzip", "snappy", "lz4", "zstd"]

    compressors = []
    for algo in algorithms:
        algo = algo.lower()
        if algo not in ALGORITHM_MAP:
            typer.echo(f"Error: Unsupported algorithm '{algo}'. Supported: {list(ALGORITHM_MAP.keys())}")
            raise typer.Exit(code=1)

        if algo == "zstd":
            levels = zstd_levels if zstd_levels else [3]  # default to level 3 if none provided
            for level in levels:
                if not (1 <= level <= 22):
                    typer.echo(f"Error: zstd-level {level} is out of range (1–22).")
                    raise typer.Exit(code=1)
                compressors.append(ZstdCompressor(level=level))
        else:
            compressors.append(ALGORITHM_MAP[algo]())

    results = run_benchmarks(input_file, compressors)

    output_results(results, output_format)


@app.command()
def version():
    """Show the installed version."""
    print(f"compressbench version {__version__}")


if __name__ == "__main__":
    app()
