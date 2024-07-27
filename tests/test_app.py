import pytest
import pandas as pd
from app import load_data, monthly_revenue, product_revenue, customer_revenue, top_customers

@pytest.fixture
def sample_data():
    data = {
        'order_id': [1, 2, 3, 4, 5],
        'customer_id': [101, 102, 103, 101, 102],
        'order_date': ['2023-01-01', '2023-02-01', '2023-02-15', '2023-03-01', '2023-03-15'],
        'product_id': [201, 202, 203, 201, 202],
        'product_name': ['Product A', 'Product B', 'Product C', 'Product A', 'Product B'],
        'product_price': [100, 200, 150, 100, 200],
        'quantity': [1, 2, 1, 3, 2]
    }
    return pd.DataFrame(data)

def test_monthly_revenue(sample_data):
    result = monthly_revenue(sample_data)
    assert len(result) == 3

def test_product_revenue(sample_data):
    result = product_revenue(sample_data)
    assert len(result) == 3

def test_customer_revenue(sample_data):
    result = customer_revenue(sample_data)
    assert len(result) == 3

def test_top_customers(sample_data):
    result = top_customers(sample_data)
    assert len(result) == 3
