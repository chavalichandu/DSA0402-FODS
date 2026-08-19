import pandas as pd

# Sales data
data = {
    "Customer": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Age": [20, 25, 20, 30, 25, 20, 35, 30]
}

# Create DataFrame
df = pd.DataFrame(data)

# Frequency distribution
frequency = df["Age"].value_counts().sort_index()

print("Frequency Distribution of Customer Ages:")
print(frequency)
