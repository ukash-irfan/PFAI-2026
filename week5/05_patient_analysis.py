import numpy as np

patient_data = np.array([
    [101, 45, 38.5, 100, 92],
    [102, 23, 36.8, 75, 98],
    [103, 67, 39.1, 110, 89],
    [104, 54, 37.0, 80, 96],
    [105, 34, 38.0, 95, 93],
    [106, 72, 36.5, 70, 97],
], dtype=float)
#E1
print(f"Shape: {patient_data.shape}, ndim: {patient_data.ndim}, Size: {patient_data.size}, dtype: {patient_data.dtype}")
#E2
patient_ids = patient_data[:, 0].astype(int)
clinical_features = patient_data[:, 1:]
print("Patient IDs:", patient_ids)
age = clinical_features[:, 0]
temperature = clinical_features[:, 1] 
blood_pressure = clinical_features[:, 2]
oxygen_saturation = clinical_features[:, 3]
print("Age:", age)
print("Temperature:", temperature)
print("Blood Pressure:", blood_pressure)
print("Oxygen Saturation:", oxygen_saturation)
#E3
avg_age = np.mean(clinical_features[:, 0])
print(f"Average Age: {avg_age:.2f}")
clinical_means = np.mean(clinical_features, axis=0)
print("Clinical Means (Age, Temp, HR, O2):", clinical_means)
print("Average Temperature:", clinical_means[1])
print("Average Blood Pressure:", clinical_means[2])
print("Average Oxygen Saturation:", clinical_means[3])
#E4
older_patients = patient_data[patient_data[:, 1] > 60]
print("Older Patients (Age > 60):\n", older_patients)

hotter_patients = patient_data[patient_data[:, 2] > 38.0]
print("Hotter Patients (Temp > 38.0):\n", hotter_patients)

oxygen_below_94 = patient_data[patient_data[:, 4] < 94]
print("Oxygen Saturation Below 94:\n", oxygen_below_94)
#E5
high_risk_mask = (temperature > 38.0) & (oxygen_saturation < 94)
print(f"count of high-risk: {np.count_nonzero(high_risk_mask)}")
print(f"High-Risk Patients Mask: {high_risk_mask}")
#E6
clinical_features_normalized = (clinical_features - clinical_features.min(axis=0)) / (clinical_features.max(axis=0) - clinical_features.min(axis=0))
print("Normalized Clinical Features:\n", clinical_features_normalized)

np.save("week05/data/patient_data.npy", patient_data)
loaded_npy = np.load("week05/data/patient_data.npy")
np.savetxt("week05/output/normalized_features.csv", clinical_features_normalized, delimiter=",", fmt="%.4f") 
loaded_csv = np.loadtxt("week05/output/normalized_features.csv", delimiter=",") 