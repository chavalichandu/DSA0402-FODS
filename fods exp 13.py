import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
data = pd.read_csv("stock_data.csv")

# Get closing prices
prices = data["Close"]

# Calculate variability
mean = prices.mean()
variance = prices.var()
std = prices.std()

# Minimum and maximum
minimum = prices.min()
maximum = prices.max()

print("Mean Price:", round(mean, 2))
print("Variance:", round(variance, 2))
print("Standard Deviation:", round(std, 2))
print("Minimum Price:", minimum)
print("Maximum Price:", maximum)

# Plot stock prices
plt.plot(prices, marker='o')
plt.title("Stock Closing Prices")
plt.xlabel("Trading Day")
plt.ylabel("Closing Price")
plt.grid(True)
plt.show()
