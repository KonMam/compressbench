import zstandard as zstd

from compressbench.compressors.base import Compressor


class ZstdCompressor(Compressor):
    name = "zstd"

    def compress(self, input_file: str) -> bytes:
        import pyarrow.parquet as pq

        table = pq.read_table(input_file)
        data = table.to_pandas().to_parquet(index=False)

        cctx = zstd.ZstdCompressor()

        return cctx.compress(data)

    def decompress(self, compressed_data: bytes) -> bytes:
        dctx = zstd.ZstdDecompressor()

        return dctx.decompress(compressed_data)
