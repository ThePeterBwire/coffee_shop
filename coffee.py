class Coffee:
    """A coffee type that can be ordered.
    
    Attributes:
        name (str): The coffee's name (at least 3 characters)
    """
    
    all = []
    
    def __init__(self, name):
        """Initialize a coffee with its name.
        
        Args:
            name (str): The coffee's name (at least 3 characters)
            
        Raises:
            TypeError: If name is not a string
            ValueError: If name is too short
        """
        self.name = name
        Coffee.all.append(self)
        
    @property
    def name(self):
        """The name property."""
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters")
        self._name = value
        
    def orders(self):
        """Returns a list of all orders for this coffee."""
        from order import Order
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        """Returns a unique list of customers who ordered this coffee."""
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        """Returns the total number of times this coffee has been ordered."""
        return len(self.orders())
    
    def average_price(self):
        """Returns the average price for this coffee based on its orders."""
        prices = [order.price for order in self.orders()]
        if not prices:
            return 0
        return sum(prices) / len(prices)
    
    def __repr__(self):
        return f"<Coffee name={self.name}>"