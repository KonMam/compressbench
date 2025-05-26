from dataclasses import dataclass


@dataclass
class BenchmarkResult:
    algorithm: str
    original_size: int
    compressed_size: int
    compression_ratio: float
    compression_time: float
    decompression_time: float
    compression_throughput: float
    decompression_throughput: float
    input_file: str
