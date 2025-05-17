import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def test_valid_creation(self):
        customer = Customer("Alice")
        assert customer.name == "Alice"
        assert customer in Customer.all
    
    @pytest.mark.parametrize("invalid_name,exception", [
        (123, TypeError),
        ("", ValueError),
        ("ThisNameIsWayTooLong", ValueError),
        (None, TypeError)
    ])
    def test_invalid_names(self, invalid_name, exception):
        with pytest.raises(exception):
            Customer(invalid_name)
    
    def test_orders_relationship(self, sample_customer, sample_coffee):
        order1 = Order(sample_customer, sample_coffee, 5.0)
        order2 = Order(sample_customer, sample_coffee, 6.0)
        assert len(sample_customer.orders()) == 2
        assert order1 in sample_customer.orders()
        assert order2 in sample_customer.orders()
    
    def test_coffees_unique(self, sample_customer):
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Espresso")
        Order(sample_customer, coffee1, 5.0)
        Order(sample_customer, coffee1, 6.0)
        Order(sample_customer, coffee2, 4.0)
        assert len(sample_customer.coffees()) == 2
    
    def test_create_order(self, sample_customer, sample_coffee):
        order = sample_customer.create_order(sample_coffee, 5.0)
        assert order in sample_customer.orders()
        assert order.coffee == sample_coffee
        assert order.price == 5.0
    
    def test_most_aficionado(self):
        coffee = Coffee("Mocha")
        customer1 = Customer("Big Spender")
        customer2 = Customer("Small Spender")
        Order(customer1, coffee, 9.0)
        Order(customer1, coffee, 8.0)
        Order(customer2, coffee, 5.0)
        assert Customer.most_aficionado(coffee) == customer1
    
    def test_most_aficionado_no_orders(self):
        coffee = Coffee("New Blend")
        assert Customer.most_aficionado(coffee) is None