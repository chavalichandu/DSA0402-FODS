import numpy as np

bedrooms = np.array([3, 5, 4, 6, 2, 5, 7])
sale_price = np.array([250000, 450000, 350000, 600000, 200000, 500000, 700000])

prices = sale_price[bedrooms > 4]

average_price = np.mean(prices)

print("Average Sale Price:", average_price)
