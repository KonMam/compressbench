import snappy

from compressbench.compressors.base import Compressor


class SnappyCompressor(Compressor):
    name = "snappy"

    def compress(self, input_file: str) -> bytes:
        import pyarrow.parquet as pq

        table = pq.read_table(input_file)
        data = table.to_pandas().to_parquet(index=False)

        return snappy.compress(data)

    def decompress(self, compressed_data: bytes) -> bytes:
        return snappy.decompress(compressed_data)
