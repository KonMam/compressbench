import io
import pyarrow.parquet as pq
from compressbench.compressors.base import Compressor

class SnappyCompressor(Compressor):
    name = "snappy"

    def compress(self, input_file: str) -> bytes:
        table = pq.read_table(input_file)
        buffer = io.BytesIO()
        pq.write_table(table, buffer, compression="snappy")
        return buffer.getvalue()

    def decompress(self, compressed_data: bytes) -> bytes:
        table = pq.read_table(io.BytesIO(compressed_data))
        out_buffer = io.BytesIO()
        pq.write_table(table, out_buffer, compression=None)
        return out_buffer.getvalue()
