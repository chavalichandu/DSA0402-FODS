import numpy as np
from scipy.stats import ttest_ind

# Conversion rate data
A = [4.5, 5.2, 4.8, 5.1, 4.9, 5.3, 4.7, 5.0, 4.6, 5.1]

B = [5.5, 5.8, 5.2, 5.9, 5.6, 5.7, 5.4, 5.8, 5.3, 5.6]

# Calculate mean
print("Mean of A:", np.mean(A))
print("Mean of B:", np.mean(B))

# Perform t-test
t, p = ttest_ind(A, B)

print("T-value:", t)
print("P-value:", p)

# Decision
if p < 0.05:
    print("There is a statistically significant difference.")
else:
    print("There is no statistically significant difference.")
