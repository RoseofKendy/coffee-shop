from customer import Customer
from coffee import Coffee
from order import Order

# Create some customers
customer1 = Customer("Alice")
customer2 = Customer("Bob")

# Create some coffees
coffee1 = Coffee("Latte")
coffee2 = Coffee("Cappuccino")
coffee3 = Coffee("Espresso")

# Create some orders
order1 = Order(customer1, coffee1, 5.0)
order2 = Order(customer1, coffee2, 4.5)
order3 = Order(customer2, coffee1, 6.0)
order4 = Order(customer2, coffee3, 3.5)

# Test relationships
print(f"{customer1.name}'s orders: {[o.coffee.name for o in customer1.orders()]}")
print(f"{customer1.name}'s coffees: {[c.name for c in customer1.coffees()]}")
print(f"{coffee1.name}'s orders count: {coffee1.num_orders()}")
print(f"{coffee1.name}'s average price: {coffee1.average_price():.2f}")

# Test most_aficionado
top_customer = Customer.most_aficionado(coffee1)
print(f"Biggest spender on {coffee1.name}: {top_customer.name if top_customer else 'None'}")