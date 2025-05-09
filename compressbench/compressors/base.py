from abc import ABC, abstractmethod

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

        table = pq.read_table(input_file)
        data = table.to_pandas().to_parquet(index=False)

        original_size = len(data)

        start = time.perf_counter()
        compressed_data = self.compress(input_file)
        compression_time = time.perf_counter() - start

        compressed_size = len(compressed_data)

        start = time.perf_counter()
        decompressed_data = self.decompress(compressed_data)  # remove unused variable later?
        decompression_time = time.perf_counter() - start

        return BenchmarkResult(
            algorithm=self.name,
            compression_ratio=original_size / compressed_size if compressed_size > 0 else 0,
            compression_time=compression_time,
            decompression_time=decompression_time,
            input_file=input_file,
        )
