import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("data.csv")

# Stop words
stop_words = {
    "the", "and", "is", "a", "an", "to",
    "of", "in", "for", "on", "this", "that",
    "it", "was", "are", "with"
}

# Combine all feedback
text = " ".join(df["feedback"].astype(str))

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans("", "", string.punctuation))

# Split into words
words = text.split()

# Remove stop words
words = [word for word in words if word not in stop_words]

# Count words
frequency = Counter(words)

# Get N from user
n = int(input("Enter N: "))

# Top N words
top_words = frequency.most_common(n)

print("\nTop", n, "Most Frequent Words:")
for word, count in top_words:
    print(word, ":", count)

# Bar graph
words = [x[0] for x in top_words]
counts = [x[1] for x in top_words]

plt.bar(words, counts)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top Frequent Words in Customer Feedback")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
