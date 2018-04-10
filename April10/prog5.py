import numpy as np
import pandas as pd

dataset = pd.read_excel("prog5.xlsx")

print("Summary Statistics:")
print(dataset.describe())

print("\nSummary statistics for unit price")
print(dataset['Unit price'].describe())

print("\nDatatype used for each field")
print(dataset.dtypes)

print("\nDataframe called customers containing name and ext price")
customers = dataset.iloc[:, [1,6]]
print(customers)