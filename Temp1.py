import sys
import numpy as np
import pandas as pd

print("Python version:", sys.version)
print("NumPy version:", np.__version__)
print("Pandas version:", pd.__version__)

# List
fruits = ["apple", "banana", "mango"]
print("\nList:", fruits)

# Tuple
marks = (85, 90, 78)
print("Tuple:", marks)

# Set
unique_numbers = {1, 2, 2, 3, 4}
print("Set (duplicates removed):", unique_numbers)

student = {
    "name": "Vishnu",
    "age": 20,
    "branch": "IT"
}
print("Dictionary:", student)


arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print("\n1D Array:", arr1)
print("2D Array:\n", arr2)
print("\nArray shape:", arr2.shape)
print("Array sum:", arr2.sum())

print("Element-wise addition:", arr1 + 5)
print("Array * 2:\n", arr2 * 2)

data = {
    "Name": ["Amit", "Neha", "Rohit", "Priya"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)


print("\nFirst 2 rows:")
print(df.head(2))


print("\nAverage marks:", df["Marks"].mean())

print("\nStudents with marks > 80:")
print(df[df["Marks"] > 80])
