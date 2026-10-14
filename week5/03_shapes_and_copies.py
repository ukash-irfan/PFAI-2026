import numpy as np

original = np.array([10, 20, 30, 40, 50])
view = original[1:4]
view[0] = 999
print("C1 - Original after modifying view:", original)
original = np.array([10, 20, 30, 40, 50])
independent = original[1:4].copy()
independent[0] = 999
print("C2 - Original after modifying independent copy:", original)
print("C2 - Independent copy:", independent)
values = np.arange(1, 13)
reshaped_3x4 = values.reshape(3, 4)
transposed = reshaped_3x4.T
flattened = reshaped_3x4.flatten()
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
vstack_arr = np.vstack((arr1, arr2))
hstack_arr = np.hstack((arr1, arr2))
split_parts = np.split(np.arange(12), 3)
print("\n--- C3 Shapes ---")
print("Reshaped 3x4 shape:", reshaped_3x4.shape)
print("Transposed shape:", transposed.shape)
print("Flattened shape:", flattened.shape)
print("VStack shape:", vstack_arr.shape)
print("HStack shape:", hstack_arr.shape)
print("Split parts shapes:", [p.shape for p in split_parts])