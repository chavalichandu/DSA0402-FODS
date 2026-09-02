import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

# Read dataset
df = pd.read_csv("bank-additional-full.csv", sep=None, engine="python")

# Clean column names
df.columns = df.columns.str.strip()

# Take 20 customers
df = df.head(20)

print("Columns in dataset:")
print(df.columns.tolist())

# Find target column
target = "y"

# Convert text columns to numbers
for c in df.select_dtypes(include=["object", "string"]).columns:
    df[c] = LabelEncoder().fit_transform(df[c].astype(str))

# Remove target and duration if they exist
X = df.drop(columns=[c for c in ["y", "duration"] if c in df.columns])
y = df[target]

# Models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "KNN": KNeighborsClassifier()
}

print("\nModel Results:")

for name, model in models.items():
    model.fit(X, y)
    prediction = model.predict(X)
    print(name, "Accuracy:", accuracy_score(y, prediction))

# K-Means
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X)

print("\nCustomer Clusters:")
print(df[["age", "Cluster"]])

# Graph 1 - Subscription
plt.figure()
df["y"].value_counts().plot(kind="bar")
plt.xlabel("Subscription")
plt.ylabel("Customers")
plt.title("Subscribed vs Not Subscribed")
plt.show()

# Graph 2 - Age and Cluster
plt.figure()
plt.scatter(df["age"], df["Cluster"])
plt.xlabel("Age")
plt.ylabel("Cluster")
plt.title("Customer Segmentation")
plt.show()

print("\nProgram completed successfully!")
