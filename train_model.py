from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train a simple RandomForest model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Save the model to a file
with open("iris_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model saved as iris_model.pkl")
