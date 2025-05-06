import typer

from compressbench import __version__

app = typer.Typer(help="Benchmark compression algorithms on Parquet datasets.")


@app.command()
def benchmark(
    input_file: str = typer.Argument(..., help="Path to the Parquet file to benchmark."),
    algorithms: list[str] = typer.Option(
        None, "--algorithms", "-a", help="Compression algorithms to test (gzip, snappy, lz4, zstd)."
    ),
    # level: int = typer.Option(
    #     None, "--level", "-l", help="Compression level (if supported by the chosen algorithm(s))."
    # # ),
    # output_format: str = typer.Option("text", "--output-format", "-o", help="Output format: text, json, csv."),
):
    """
    Run compression benchmark on the specified Parquet file.
    """
    pass


@app.command()
def version():
    """Show the installed version."""
    print(f"compressbench version {__version__}")


if __name__ == "__main__":
    app()
