import gzip

from compressbench.compressors.base import Compressor


class GzipCompressor(Compressor):
    name = "gzip"

    def compress(self, input_file: str) -> bytes:
        import pyarrow.parquet as pq

        table = pq.read_table(input_file)
        data = table.to_pandas().to_parquet(index=False)

        return gzip.compress(data)

    def decompress(self, compressed_data: bytes) -> bytes:
        return gzip.decompress(compressed_data)
