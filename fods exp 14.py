import pandas as pd
import matplotlib.pyplot as plt

# Data
study_time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
scores = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# Create DataFrame
df = pd.DataFrame({
    "Study Time": study_time,
    "Exam Score": scores
})

# Calculate correlation
correlation = df["Study Time"].corr(df["Exam Score"])

print("Correlation coefficient:", round(correlation, 2))

# Scatter plot
plt.scatter(study_time, scores)
plt.xlabel("Study Time (Hours)")
plt.ylabel("Exam Score")
plt.title("Study Time vs Exam Score")
plt.grid(True)
plt.show()
