import pandas as pd

orders = {
    "OrderID": [101, 102, 103, 104, 105],
    "Customer": ["Alice", "Bob", "Alice", "Charlie", "Bob"],
    "Product": ["Laptop", "Mouse", "Keyboard", "Laptop", "Mouse"],
    "Quantity": [1, 2, 1, 1, 3],
    "Price": [1200, 25, 75, 1200, 25]
}

df = pd.DataFrame(orders)

df["Total"] = df["Quantity"] * df["Price"]

print(df)
