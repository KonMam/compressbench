# compressbench

**Benchmark compression algorithms on Parquet datasets.**

## Why

Compression settings affect performance, storage cost, and latency — but most data engineers inherit defaults without testing.
`compressbench` lets you benchmark compression ratio, compression speed, and decompression speed across algorithms using your own Parquet files.

## Features

- Accepts local Parquet files as input.
- Supports gzip and snappy.
- Outputs:
    - Compression ratio.
    - Compression time.
    - Decompression time.
- CLI built with Typer.
- Unit tests with pytest.

## Installation

```bash
pip install compressbench
```

## Usage

```bash
compressbench benchmark tests/data/test_data.parquet --a gzip -a snappy --output-format text
```

```
Algorithm: gzip
Compression ratio: 2.48
Compression time: 0.00s
Decompression time: 0.00s
Input file: tests/data/test_data.parquet
----------------------------------------
Algorithm: snappy
Compression ratio: 1.89
Compression time: 0.00s
Decompression time: 0.00s
Input file: tests/data/test_data.parquet
----------------------------------------
```

## CLI Options
input.parquet   Path to the Parquet file to benchmark.
--algorithms    List of algorithms to test (gzip, snappy).
--level         Not supported in v0.1.0. Reserved for future versions.

## Roadmap
See ROADMAP.md for planned features.

## License
MIT
