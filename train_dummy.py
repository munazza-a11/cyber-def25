import pickle
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# 1. Generate dummy data (Log Feature 1, Log Feature 2) -> 0 (Safe), 1 (Malware)
X = np.array([[10, 2], [50, 4], [10, 1], [90, 10], [85, 12]])
y = np.array([0, 0, 0, 1, 1])

# 2. Train a simple model
clf = RandomForestClassifier()
clf.fit(X, y)

# 3. Save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(clf, f)

print("Dummy model.pkl created successfully!")
