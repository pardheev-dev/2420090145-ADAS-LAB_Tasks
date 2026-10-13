# PROGRAM 9: Road Surface Classification System
# Classifies the road surface as Smooth or Rough from sensor readings using KNN.

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Features: [vertical vibration (g), suspension travel (mm), wheel speed variance]
X_train = [
    [0.12, 4.0, 0.03], [0.15, 5.2, 0.05], [0.10, 3.6, 0.02], [0.18, 6.0, 0.06],
    [0.14, 4.8, 0.04], [0.11, 3.9, 0.03], [0.16, 5.5, 0.05], [0.13, 4.4, 0.04],
    [0.62, 18.0, 0.28], [0.75, 22.5, 0.35], [0.58, 16.4, 0.25], [0.81, 25.0, 0.40],
    [0.69, 20.1, 0.31], [0.55, 15.8, 0.24], [0.88, 27.3, 0.44], [0.71, 21.2, 0.33],
]
y_train = ["Smooth"] * 8 + ["Rough"] * 8

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# New sensor readings
X_test = [
    [0.13, 4.5, 0.03],
    [0.70, 21.0, 0.32],
    [0.17, 5.8, 0.06],
    [0.85, 26.0, 0.42],
]
y_test = ["Smooth", "Rough", "Smooth", "Rough"]

predictions = model.predict(X_test)

for features, predicted in zip(X_test, predictions):
    vib, travel, var = features
    action = "Reduce speed / stiffen suspension" if predicted == "Rough" else "Normal driving"
    print(f"vib={vib:.2f}g  travel={travel:5.1f}mm  var={var:.2f}  ->  {predicted:6s} | {action}")

print("\nAccuracy:", accuracy_score(y_test, predictions))
