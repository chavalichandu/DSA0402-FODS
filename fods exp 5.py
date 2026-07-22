import numpy as np

fuel_efficiency = np.array([15, 18, 20, 22, 25])

average = np.mean(fuel_efficiency)
print("Average Fuel Efficiency:", average, "km/l")

percentage_improvement = ((fuel_efficiency - fuel_efficiency[0]) / fuel_efficiency[0]) * 100

print("Percentage Improvement:")
print(percentage_improvement)
