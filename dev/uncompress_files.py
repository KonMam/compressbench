import pyarrow.parquet as pq

table = pq.read_table("tests/data/fhvhv_tripdata_2024-03.parquet")

pq.write_table(table, "tests/data/fhvhv_tripdata_2024-03_uncompressed.parquet", compression=None)
