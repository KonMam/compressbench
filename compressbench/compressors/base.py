from abc import ABC, abstractmethod
from pathlib import Path

from compressbench.types import BenchmarkResult


class Compressor(ABC):
    name: str

    @abstractmethod
    def compress(self, input_file: str) -> bytes:
        pass

    @abstractmethod
    def decompress(self, compressed_data: bytes) -> bytes:
        pass

    def benchmark(self, input_file: str) -> BenchmarkResult:
        """Default benchmarking logic that most compressors can use."""
        import time

        import pyarrow.parquet as pq

        original_size = Path(input_file).stat().st_size

        start = time.perf_counter()
        compressed_data = self.compress(input_file)
        compression_time = time.perf_counter() - start

        compressed_size = len(compressed_data)

        start = time.perf_counter()
        self.decompress(compressed_data)
        decompression_time = time.perf_counter() - start

        return BenchmarkResult(
            algorithm=self.name,
            original_size=original_size,
            compressed_size=compressed_size,
            compression_ratio=original_size / compressed_size if compressed_size > 0 else 0,
            compression_time=compression_time,
            decompression_time=decompression_time,
            input_file=input_file,
        )
