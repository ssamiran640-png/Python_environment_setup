import numpy as np

# Internal marks of 10 students
marks = np.array([78, 85, 67, 92, 74, 88, 69, 95, 81, 73])

# Calculate statistics
mean = np.mean(marks)
median = np.median(marks)
std_dev = np.std(marks)
maximum = np.max(marks)
minimum = np.min(marks)

# Print results
print("Marks:", marks)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Maximum:", maximum)
print("Minimum:", minimum)