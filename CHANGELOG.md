# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]

### Added
- LZ4 and zstd support.

### Changed

### Removed

---

## [0.1.0] - 2025-05-09

### Added
- CLI endpoints:
    - Accept Parquet input.
    - Select compression algorithm(s).
- Output:
    - Compression ratio.
    - Compression time.
    - Decompression time.
- Supported algorithms:
    - gzip
    - snappy
- Output formats:
    - --output-format text (default)
    - --output-format json
    - --output-format csv
- Pytests

