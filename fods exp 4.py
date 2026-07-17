import numpy as np

sales = np.array([12000, 15000, 18000, 21000, 25000])

total_sales = np.sum(sales)

percentage_increase = ((sales[1:] - sales[:-1]) / sales[:-1]) * 100

print("Monthly Sales:", sales)
print("Total Sales:", total_sales)
print("Percentage Increase:", percentage_increase)
