import numpy as np

data = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])
first_row = data[0, :]
last_col = data[:, -1]
middle_block = data[1:3, 1:3]
every_second_row = data[::2, :]
gt_75 = data[data > 75]
div_by_20 = data[data % 20 == 0]
print("First Row:\n", first_row)
print("Last Column:\n", last_col)
print("Middle 2x2 Block:\n", middle_block)
print("Every Second Row:\n", every_second_row)
print("Values > 75:\n", gt_75)
print("Values divisible by 20:\n", div_by_20)