import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Mouse", "Laptop", "Monitor", "Mouse", "Keyboard"],
    "Quantity": [2, 5, 3, 4, 1, 2, 6, 2]
}

df = pd.DataFrame(data)

top_5_products = (
    df.groupby("Product")["Quantity"]
      .sum()
      .sort_values(ascending=False)
      .head(5)
)

print("Top 5 Most Sold Products:")
print(top_5_products)
