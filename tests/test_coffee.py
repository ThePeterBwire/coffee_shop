import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee:
    def test_valid_creation(self):
        coffee = Coffee("Latte")
        assert coffee.name == "Latte"
        assert coffee in Coffee.all
    
    @pytest.mark.parametrize("invalid_name,exception", [
        (123, TypeError),
        ("A", ValueError),
        ("  ", ValueError),
        (None, TypeError)
    ])
    def test_invalid_names(self, invalid_name, exception):
        with pytest.raises(exception):
            Coffee(invalid_name)
    
    def test_orders_relationship(self, sample_coffee, sample_customer):
        order1 = Order(sample_customer, sample_coffee, 5.0)
        order2 = Order(sample_customer, sample_coffee, 6.0)
        assert len(sample_coffee.orders()) == 2
        assert order1 in sample_coffee.orders()
        assert order2 in sample_coffee.orders()
    
    def test_customers_unique(self, sample_coffee):
        customer = Customer("Regular")
        Order(customer, sample_coffee, 5.0)
        Order(customer, sample_coffee, 6.0)
        assert len(sample_coffee.customers()) == 1
    
    def test_num_orders(self, sample_coffee):
        assert sample_coffee.num_orders() == 0
        customer = Customer("Test")
        Order(customer, sample_coffee, 5.0)
        assert sample_coffee.num_orders() == 1
    
    def test_average_price(self, sample_coffee):
        customer = Customer("Test")
        Order(customer, sample_coffee, 4.0)
        Order(customer, sample_coffee, 6.0)
        assert sample_coffee.average_price() == 5.0
    
    def test_average_price_no_orders(self, sample_coffee):
        assert sample_coffee.average_price() == 0