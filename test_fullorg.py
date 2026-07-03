from fullorg import make_headings

#expected results, len of the list
def test_make_headings():
    expected = [
        "transaction_id", "timestamp", "store_id", "product_id",
        "quantity", "unit_price", "total_amount", "payment_method"
    ]

    result = make_headings()

    assert isinstance(result, list)
    assert result == expected
    assert len(result) == 8

#correct length, type correction
from fullorg import make_row

def test_make_row():
    row = make_row()

    assert isinstance(row, list)
    assert len(row) == 8

    transaction_id, timestamp, store_id, product_id, quantity, unit_price, total_amount, payment_method = row

    assert isinstance(transaction_id, int)
    assert isinstance(store_id, int)
    assert isinstance(product_id, int)
    assert isinstance(quantity, int)
    assert isinstance(unit_price, float)
    assert isinstance(total_amount, float)
    assert payment_method in ["cash", "credit_card", "debit_card", "mobile_pay", "online"]

    assert round(quantity * unit_price, 2) == total_amount


# correct number of rows
from fullorg import make_data
def test_make_data():
    rows = 10
    data = make_data(rows)

    assert isinstance(data, list)
    assert len(data) == rows

    for row in data:
        assert isinstance(row, list)
        assert len(row) == 8

#new file created, correct headers, prevent overide
from fullorg import make_file
import os

def test_make_file_creates_file(tmp_path):
    file_path = tmp_path / "test_sales.csv"

    headings = make_headings()
    data = make_data(3)

    result = make_file(str(file_path), headings, data)

    assert result is True
    assert file_path.exists()

    with open(file_path, "r") as f:
        content = f.read()
        assert "transaction_id" in content

#file created and functions work without errors
from fullorg import build_me
import glob

def test_build_me():
    build_me()

    files = glob.glob("SALES_DATA_*.csv")

    assert len(files) >= 1
