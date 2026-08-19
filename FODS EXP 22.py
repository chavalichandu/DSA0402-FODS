import numpy as np
from scipy import stats

# Blood pressure reduction data
drug = [12, 15, 10, 14, 13, 16, 11, 15, 14, 12]
placebo = [5, 7, 4, 6, 5, 8, 6, 4, 7, 5]

# 95% Confidence Interval
drug_ci = stats.t.interval(
    0.95, len(drug)-1,
    loc=np.mean(drug),
    scale=stats.sem(drug)
)

placebo_ci = stats.t.interval(
    0.95, len(placebo)-1,
    loc=np.mean(placebo),
    scale=stats.sem(placebo)
)

print("Drug Mean:", np.mean(drug))
print("95% CI for Drug:", drug_ci)

print("\nPlacebo Mean:", np.mean(placebo))
print("95% CI for Placebo:", placebo_ci)
