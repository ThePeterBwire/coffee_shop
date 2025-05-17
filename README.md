# Coffee Shop Domain Model

A Python implementation of a coffee shop domain with Customer, Coffee, and Order classes.

## Features

- Customer management with name validation
- Coffee menu items with name validation
- Order tracking with price validation
- Relationship methods between all entities
- Comprehensive test coverage
- Interactive debug console

## Installation

```bash
pipenv install
pipenv install --dev pytest
```

## Running Tests

```bash
pipenv run pytest
```

## Interactive Debugging

```bash
python debug.py
```

## Example Usage

```python
from customer import Customer
from coffee import Coffee
from order import Order

# Create instances
customer = Customer("Alice")
coffee = Coffee("Latte")

# Place an order
order = Order(customer, coffee, 5.0)

# Alternative way to create order
order2 = customer.create_order(coffee, 4.5)

# Get customer's coffee preferences
print(customer.coffees())  # [<Coffee name=Latte>]

# Get coffee's customers
print(coffee.customers())  # [<Customer name=Alice>]

# Get business insights
print(coffee.num_orders())  # 2
print(coffee.average_price())  # 4.75

# Find top customer for a coffee
top_customer = Customer.most_aficionado(coffee)
print(top_customer)  # <Customer name=Alice>
```

## Class Diagram

```
Customer *-- Order
Coffee *-- Order
```

- A Customer can have many Orders
- A Coffee can have many Orders
- Each Order belongs to one Customer and one Coffee# coffee_shop
