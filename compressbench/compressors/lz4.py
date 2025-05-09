import lz4.frame

from compressbench.compressors.base import Compressor


class Lz4Compressor(Compressor):
    name = "lz4"

    def compress(self, input_file: str) -> bytes:
        import pyarrow.parquet as pq

        table = pq.read_table(input_file)
        data = table.to_pandas().to_parquet(index=False)

        return lz4.frame.compress(data)

    def decompress(self, compressed_data: bytes) -> bytes:
        return lz4.frame.decompress(compressed_data)
