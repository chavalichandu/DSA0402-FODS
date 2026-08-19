import pandas as pd

# Likes data
data = {
    "Post": [1, 2, 3, 4, 5, 6, 7, 8],
    "Likes": [100, 150, 100, 200, 150, 100, 250, 200]
}

# Create DataFrame
df = pd.DataFrame(data)

# Frequency distribution
frequency = df["Likes"].value_counts().sort_index()

print("Frequency Distribution of Likes:")
print(frequency)
