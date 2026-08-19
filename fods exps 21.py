import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

age = [25,30,22,35,28,40,32,27,45,38,29,31,24,36,42,33,26,39]

fat = [18.5,22.1,15.2,25.4,20.3,28.5,24.1,19.2,30.1,
       26.4,21.5,23.2,17.8,27.1,29.3,24.8,18.9,26.7]

df = pd.DataFrame({"Age": age, "%Fat": fat})

print("Mean:\n", df.mean())
print("\nMedian:\n", df.median())
print("\nStandard Deviation:\n", df.std())

# Boxplots
df.boxplot()
plt.title("Boxplot")
plt.show()

# Scatter plot
plt.scatter(age, fat)
plt.xlabel("Age")
plt.ylabel("Body Fat")
plt.title("Age vs Body Fat")
plt.show()

# Q-Q plots
stats.probplot(age, dist="norm", plot=plt)
plt.title("Q-Q Plot - Age")
plt.show()

stats.probplot(fat, dist="norm", plot=plt)
plt.title("Q-Q Plot - Body Fat")
plt.show()
