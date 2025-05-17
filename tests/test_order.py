import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder:
    def test_valid_creation(self, sample_customer, sample_coffee):
        order = Order(sample_customer, sample_coffee, 5.0)
        assert order.customer == sample_customer
        assert order.coffee == sample_coffee
        assert order.price == 5.0
        assert order in Order.all
    
    @pytest.mark.parametrize("invalid_price,exception", [
        ("five", TypeError),
        (0.5, ValueError),
        (10.5, ValueError),
        (-1.0, ValueError),
        (None, TypeError)
    ])
    def test_invalid_prices(self, invalid_price, exception, sample_customer, sample_coffee):
        with pytest.raises(exception):
            Order(sample_customer, sample_coffee, invalid_price)
    
    def test_invalid_customer(self, sample_coffee):
        with pytest.raises(TypeError):
            Order("Not a customer", sample_coffee, 5.0)
    
    def test_invalid_coffee(self, sample_customer):
        with pytest.raises(TypeError):
            Order(sample_customer, "Not a coffee", 5.0)
    
    def test_relationships(self, sample_order, sample_customer, sample_coffee):
        assert sample_order in sample_customer.orders()
        assert sample_order in sample_coffee.orders()