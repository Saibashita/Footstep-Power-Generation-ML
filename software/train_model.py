import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import joblib

# Load data from each activity file
def load_file(filename, label):
    with open(filename, "r") as f:
        values = [float(x.strip()) for x in f.readlines()]
    labels = [label] * len(values)
    return values, labels

# Load all datasets
run_vals, run_lbls = load_file("running.txt", "Running")
walk_vals, walk_lbls = load_file("walking.txt", "Walking")
jump_vals, jump_lbls = load_file("jumping.txt", "Jumping")
stand_vals, stand_lbls = load_file("standing.txt", "Standing")

# Combine
X = np.array(run_vals + walk_vals + jump_vals + stand_vals).reshape(-1, 1)
y = np.array(run_lbls + walk_lbls + jump_lbls + stand_lbls)

# Train model
print("Training model...")
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Save the model
joblib.dump(model, "activity_model.pkl")
print("Model saved as activity_model.pkl")