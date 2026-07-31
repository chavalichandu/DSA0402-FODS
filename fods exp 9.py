import pandas as pd

data = {
    "Property_ID": [101, 102, 103, 104, 105],
    "Location": ["Chennai", "Bengaluru", "Chennai", "Hyderabad", "Mumbai"],
    "Price": [6500000, 8200000, 5500000, 7000000, 9000000],
    "Area": [1200, 1500, 1000, 1400, 1800],
    "Bedrooms": [3, 4, 2, 3, 4]
}

df = pd.DataFrame(data)

top5 = df.nlargest(5, "Price")
print(top5)
