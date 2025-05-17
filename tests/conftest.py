import pytest
from customer import Customer
from coffee import Coffee
from order import Order

@pytest.fixture(autouse=True)
def cleanup():
    """Clean up all instances between tests."""
    Customer.all.clear()
    Coffee.all.clear()
    Order.all.clear()

@pytest.fixture
def sample_customer():
    return Customer("Test Customer")

@pytest.fixture
def sample_coffee():
    return Coffee("Test Coffee")

@pytest.fixture
def sample_order(sample_customer, sample_coffee):
    return Order(sample_customer, sample_coffee, 5.0)