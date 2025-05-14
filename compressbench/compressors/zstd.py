import zstandard as zstd

from compressbench.compressors.base import Compressor


class ZstdCompressor(Compressor):
    def __init__(self, level: int = 3):
        self.level = level
        self.name = f"zstd (level {level})"

    def compress(self, input_file: str) -> bytes:
        import pyarrow.parquet as pq

        table = pq.read_table(input_file)
        data = table.to_pandas().to_parquet(index=False)

        cctx = zstd.ZstdCompressor(level=self.level)
        return cctx.compress(data)

    def decompress(self, compressed_data: bytes) -> bytes:
        dctx = zstd.ZstdDecompressor()
        return dctx.decompress(compressed_data)
