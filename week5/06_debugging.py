import os

import numpy as np

a = np.ones((3, 4))
b = np.ones((3, 4))
result_f1 = a + b
print("F1 Corrected:\n", result_f1)

values = np.array([10, 20, 30, 40])
selected = values[(values > 15) & (values < 35)]
print("F2 Corrected:\n", selected)

scores = np.array([[70, 80, 90], [60, 75, 85]])
student_averages = np.mean(scores, axis=1)
print("F3 Corrected:\n", student_averages)

os.makedirs("week05/data", exist_ok=True)
os.makedirs("week05/output", exist_ok=True)

patient_data = np.array([[101, 45, 38.5, 100, 92], [102, 23, 36.8, 75, 98]])
normalized_features = np.array(
    [[0.449, 0.769, 0.750, 0.333], [0.000, 0.115, 0.125, 1.000]]
)

np.save("week05/data/patient_data.npy", patient_data)
loaded_npy = np.load("week05/data/patient_data.npy")

np.savetxt(
    "week05/output/normalized_features.csv",
    normalized_features,
    delimiter=",",
    fmt="%.4f",
)
loaded_csv = np.loadtxt("week05/output/normalized_features.csv", delimiter=",")

assert np.array_equal(patient_data, loaded_npy), ".npy verification failed"
assert np.allclose(normalized_features, loaded_csv, atol=1e-4), (
    ".csv verification failed"
)

print("Save and reload verification successful!")
