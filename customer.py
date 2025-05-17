class Customer:
    """A customer who can place orders at the coffee shop.
    
    Attributes:
        name (str): The customer's name (1-15 characters)
    """
    
    all = []
    
    def __init__(self, name):
        """Initialize a customer with their name.
        
        Args:
            name (str): The customer's name (1-15 characters)
            
        Raises:
            TypeError: If name is not a string
            ValueError: If name length is invalid
        """
        self.name = name
        Customer.all.append(self)
        
    @property
    def name(self):
        """The name property."""
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value
        
    def orders(self):
        """Returns a list of all orders for this customer."""
        from order import Order
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        """Returns a unique list of coffees this customer has ordered."""
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        """Creates a new order for this customer.
        
        Args:
            coffee (Coffee): The coffee being ordered
            price (float): The price of the order (1.0-10.0)
            
        Returns:
            Order: The newly created order
        """
        from order import Order
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        """Returns the customer who has spent the most on a specific coffee.
        
        Args:
            coffee (Coffee): The coffee to check
            
        Returns:
            Customer or None: The top customer or None if no orders
        """
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("Must be a coffee instance")
            
        customers_spending = {}
        
        for order in coffee.orders():
            if order.customer in customers_spending:
                customers_spending[order.customer] += order.price
            else:
                customers_spending[order.customer] = order.price
                    
        if not customers_spending:
            return None
            
        return max(customers_spending.items(), key=lambda item: item[1])[0]
    
    def __repr__(self):
        return f"<Customer name={self.name}>"