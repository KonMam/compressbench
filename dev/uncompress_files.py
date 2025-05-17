import pyarrow.parquet as pq

table = pq.read_table("tests/data/benchmark_5gb.parquet")

pq.write_table(table, "tests/data/benchmark_5gb_uncompressed.parquet", compression=None)
