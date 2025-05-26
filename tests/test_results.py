import pytest

from compressbench.results import output_results
from compressbench.types import BenchmarkResult


@pytest.fixture
def sample_results():
    return [
        BenchmarkResult(
            algorithm="gzip",
            compression_ratio=2.5,
            compression_time=0.12,
            decompression_time=0.05,
            input_file="test_data.parquet",
            original_size=1000000,
            compressed_size=400000,
            compression_throughput=8333333.33,
            decompression_throughput=20000000.0,
        ),
        BenchmarkResult(
            algorithm="snappy",
            compression_ratio=1.7,
            compression_time=0.10,
            decompression_time=0.04,
            input_file="test_data.parquet",
            original_size=1000000,
            compressed_size=588235,
            compression_throughput=10000000.0,
            decompression_throughput=25000000.0,
        ),
    ]


def test_output_text(sample_results, capsys):
    output_results(sample_results, output_format="text")
    captured = capsys.readouterr()
    assert "Algorithm: gzip" in captured.out
    assert "Compression ratio: 2.50" in captured.out


def test_output_json(sample_results, capsys):
    output_results(sample_results, output_format="json")
    captured = capsys.readouterr()
    assert '"algorithm": "gzip"' in captured.out
    assert '"compression_ratio": 2.5' in captured.out


def test_output_csv(sample_results, capsys):
    output_results(sample_results, output_format="csv")
    captured = capsys.readouterr()
    assert (
        "algorithm,original_size,compressed_size,compression_ratio,compression_time,"
        "decompression_time,compression_throughput,decompression_throughput,input_file"
    ) in captured.out
    assert "gzip,1000000.00,400000.00,2.50" in captured.out


def test_invalid_format(sample_results):
    with pytest.raises(ValueError):
        output_results(sample_results, output_format="xml")
