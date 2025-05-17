class Order:
    """An order connecting a customer to a coffee with a price.
    
    Attributes:
        customer (Customer): The customer who placed the order
        coffee (Coffee): The coffee being ordered
        price (float): The price of the order (1.0-10.0)
    """
    
    all = []
    
    def __init__(self, customer, coffee, price):
        """Initialize an order.
        
        Args:
            customer (Customer): The customer who placed the order
            coffee (Coffee): The coffee being ordered
            price (float): The price of the order (1.0-10.0)
            
        Raises:
            TypeError: If customer or coffee are invalid types
            ValueError: If price is out of range
        """
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
        
        # Add to customer's and coffee's order lists
        customer.orders().append(self)
        coffee.orders().append(self)
        
    @property
    def price(self):
        """The price property."""
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("Price must be a number")
        if not 1.0 <= float(value) <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = float(value)
        
    @property
    def customer(self):
        """The customer property."""
        return self._customer
    
    @customer.setter
    def customer(self, value):
        from customer import Customer
        if not isinstance(value, Customer):
            raise TypeError("Customer must be an instance of Customer class")
        self._customer = value
        
    @property
    def coffee(self):
        """The coffee property."""
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if not isinstance(value, Coffee):
            raise TypeError("Coffee must be an instance of Coffee class")
        self._coffee = value
    
    def __repr__(self):
        return f"<Order customer={self.customer.name} coffee={self.coffee.name} price={self.price}>"