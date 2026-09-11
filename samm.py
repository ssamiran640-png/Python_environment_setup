import sys
import numpy as np 
import pandas as pd
marks = np.array([72,85,91,68,77])
print("Marks:", marks)
print("Mean:", np.mean(marks))
print("Maximum: ",np.max(marks))
print("Minimum: ",np.min(marks))

data={
    "Name":["Sam","Raj","Sourav","Neha"],
    "Attendance":[88,97,48,67],
    "Marks":[95,87,65,78]
}

df=pd.DataFrame(data)

print("\n--First Five Records ---")
print(df.head())
print("\n--Data Information ---")
print(df.info())
print("\n--Statistical Summary ---")
print(df.describe())

print("\nAverage Marks:", df["Marks"].mean())