import io
import pyarrow.parquet as pq
from compressbench.compressors.base import Compressor

class Lz4Compressor(Compressor):
    name = "lz4"

    def compress(self, input_file: str) -> bytes:
        table = pq.read_table(input_file)
        buffer = io.BytesIO()
        pq.write_table(table, buffer, compression="lz4")
        return buffer.getvalue()

    def decompress(self, compressed_data: bytes) -> bytes:
        table = pq.read_table(io.BytesIO(compressed_data))
        out_buffer = io.BytesIO()
        pq.write_table(table, out_buffer, compression=None)
        return out_buffer.getvalue()
