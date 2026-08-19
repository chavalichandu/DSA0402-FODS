import string

# Open the text file
file = open("sample_text.txt", "r")

# Read the text
text = file.read()

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans("", "", string.punctuation))

# Split into words
words = text.split()

# Count word frequency
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

# Display frequency
print("Word Frequency Distribution:")

for word, count in frequency.items():
    print(word, ":", count)

file.close()
