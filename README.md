# ☕ Coffee Shop - OOP Python Project

This is an object-oriented programming (OOP) project simulating a coffee shop environment using Python. The system models interactions between `Customer`, `Coffee`, and `Order` classes, and allows tracking customer orders, favorite coffees, and average coffee prices.

---

## 📂 Project Structure

Coffee-Shop/
.env # Defines the pip path to the local directory incase it causes issues on device
customer.py # Defines the Customer class
coffee.py # Defines the Coffee class
order.py # Defines the Order class
debug.py # Test script to simulate and display system functionality
Pipfile # Pipenv dependency manager file
Pipfile.lock
README.md # Project overview and setup guide


---

## 👨‍💻 Technologies Used

- **Python 3.8+**
- **Pipenv** for virtual environment and dependency management

---

## 🧩 Class Descriptions

### `Customer`
- Represents a customer in the system.
- Attributes: `name`, `_orders` list
- Methods:
  - `create_order(coffee, price)`
  - `orders()`, `coffees()`
  - `most_aficionado(coffee)`: identifies the customer who spent the most on a specific coffee.

### `Coffee`
- Represents a coffee type.
- Attributes: `name`, `_orders` list
- Methods:
  - `orders()`, `customers()`
  - `num_orders()`, `average_price()`

### `Order`
- Represents an order placed by a customer.
- Attributes: `customer`, `coffee`, `price`
- Automatically updates associated customer's and coffee's order list upon creation.

---

## 🚀 How to Run

1. **Clone the repository**:

```bash
git clone <your-repo-url>
cd Coffee-Shop
