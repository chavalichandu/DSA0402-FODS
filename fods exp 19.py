import pandas as pd
from collections import Counter

# Customer reviews
data = {
    "Review": [
        "Good product and good quality",
        "Good product and easy to use",
        "Quality product with good design"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert reviews to lowercase
text = " ".join(df["Review"]).lower()

# Split into words
words = text.split()

# Calculate frequency
frequency = Counter(words)

print("Word Frequency Distribution:")

for word, count in frequency.items():
    print(word, ":", count)
