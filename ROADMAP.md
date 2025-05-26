# ROADMAP.md

## v0.2.0

- Output summary table.
- Start adding integration tests.
- Optional: analysis notebook (`analysis.ipynb`) for saved results (CSV/JSON) visualization.
    - Bar charts: compression/decompression speeds, compression ratios.
    - Line charts: comparisons across varying data sizes.

## v0.3.0

- Parquet file generation module (simulate different data sets / sizes).
- Support for compression level (where supported by algorithms).

## Possible Future Work

- CPU and memory usage tracking (psutil / tracemalloc).
- Support for comparing custom compression algorithm implementations.
- Progress bars for long-running benchmarks.
- Support for public dataset download.
