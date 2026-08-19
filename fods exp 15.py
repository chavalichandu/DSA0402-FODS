import pandas as pd

# Read the CSV file
df = pd.read_csv("temperature.csv")

# Mean temperature
mean = df.groupby("City")["Temperature"].mean()

# Standard deviation
std = df.groupby("City")["Temperature"].std()

# Temperature range
temp_range = df.groupby("City")["Temperature"].max() - \
             df.groupby("City")["Temperature"].min()

print("Mean Temperature:")
print(mean)

print("\nStandard Deviation:")
print(std)

print("\nTemperature Range:")
print(temp_range)

# City with highest temperature range
city = temp_range.idxmax()

print("\nCity with Highest Temperature Range:", city)
print("Highest Range:", temp_range.max())
