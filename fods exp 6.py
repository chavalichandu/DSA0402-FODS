import numpy as np

quantity = np.array([2, 3, 1])

price = np.array([150, 200, 500])

item_cost = quantity * price

total_cost = np.sum(item_cost)

print("Cost of each item:", item_cost)
print("Total Purchase Cost: ₹", total_cost)
