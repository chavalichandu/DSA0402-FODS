from sklearn.neighbors import KNeighborsClassifier

X = [[1,2],[2,3],[3,4],[7,8],[8,9],[9,8]]
y = [0,0,0,1,1,1]

k = int(input("Enter k: "))
patient = [[int(input("Feature 1: ")),
            int(input("Feature 2: "))]]

model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

print("Prediction:", model.predict(patient)[0])
