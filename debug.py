from customer import Customer
from coffee import Coffee
from order import Order

def debug_interactive():
    """Interactive debug session to test the coffee shop model."""
    print("=== Coffee Shop Debug Console ===")
    
    # Clear existing data
    Customer.all.clear()
    Coffee.all.clear()
    Order.all.clear()
    
    # Create sample data
    print("\nCreating customers...")
    alice = Customer("Alice")
    bob = Customer("Bob")
    print(f"Created customers: {Customer.all}")
    
    print("\nCreating coffees...")
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    print(f"Created coffees: {Coffee.all}")
    
    # Create orders
    print("\nCreating orders...")
    order1 = Order(alice, latte, 5.0)
    order2 = Order(alice, espresso, 3.5)
    order3 = Order(bob, latte, 4.0)
    print(f"Created orders: {Order.all}")
    
    # Test relationships
    print("\nTesting relationships:")
    print(f"Alice's orders: {alice.orders()}")
    print(f"Latte's orders: {latte.orders()}")
    print(f"Alice's coffees: {alice.coffees()}")
    print(f"Latte's customers: {latte.customers()}")
    
    # Test business methods
    print("\nTesting business methods:")
    print(f"Latte order count: {latte.num_orders()}")
    print(f"Latte average price: {latte.average_price()}")
    print(f"Most aficionado for Latte: {Customer.most_aficionado(latte)}")
    
    # Test error cases
    print("\nTesting error cases...")
    try:
        bad_customer = Customer("")
    except ValueError as e:
        print(f"Caught expected error creating customer: {e}")
    
    try:
        bad_order = Order(alice, latte, 11.0)
    except ValueError as e:
        print(f"Caught expected error creating order: {e}")

if __name__ == "__main__":
    debug_interactive()