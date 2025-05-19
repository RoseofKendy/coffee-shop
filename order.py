from coffee import Coffee
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from customer import Customer

class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all_orders.append(self)
        
        # Add to customer's orders
        customer._orders.append(self)
        
        # Add to coffee's orders
        coffee._orders.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        from customer import Customer  # Local import to break circular dependency
        if not isinstance(value, Customer):
            raise ValueError("Must be a Customer instance")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise ValueError("Must be a Coffee instance")
        self._coffee = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise ValueError("Price must be a float")
        if not 1.0 <= value <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = value
