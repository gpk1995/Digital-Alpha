import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Camera.csv', sep = ';')

# properties of dataset
print(dataset.columns.values)

# datatypes of properties
print(dataset.dtypes)

# printing first 25 rows of model, release date and price
X = dataset.iloc[:25, [0, 1, -1 ]]
print(X)

# summarising the dataset
print(dataset.describe())

# summarising the statistics for price
print(dataset['Price'].describe())

# time series graph
dataset['Price'] = dataset['Price'].apply(float)
dataset = dataset['Price'] > 1000

plt.plot(dataset['Release date'], dataset['Price'] > 1000)
plt.show()

