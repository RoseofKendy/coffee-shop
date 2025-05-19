from coffee import Coffee
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from order import Order

class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        self._orders = []
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        return self._orders

    def coffees(self):
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        from order import Order  # Local import to avoid circular import
        new_order = Order(self, coffee, price)
        return new_order

    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise ValueError("Must provide a Coffee instance")
        
        if not coffee.orders():
            return None
        
        customers_spending = {}
        for order in coffee.orders():
            if order.customer in customers_spending:
                customers_spending[order.customer] += order.price
            else:
                customers_spending[order.customer] = order.price
        
        return max(customers_spending.items(), key=lambda item: item[1])[0]
