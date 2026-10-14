import numpy as np

temperatures = np.array([20, 25, 30, 35, 40])
fahrenheit = temperatures * 9/5 + 32
marks = np.array([55, 67, 72, 88, 91])
adjusted = np.minimum(marks + 5, 100)
normalized = (marks - marks.min()) / (marks.max() - marks.min())
print("Fahrenheit:", fahrenheit)
print("Adjusted Marks:", adjusted)
print("Normalized Marks:", normalized)
#D2
scores = np.array([[70, 75, 80], [60, 65, 70], [85, 90, 95]])
bonus = np.array([2, 3, 5])
adjusted_scores = scores + bonus
print("\nAdjusted Scores (Broadcasting):\n", adjusted_scores)