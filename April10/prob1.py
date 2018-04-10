import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('100 Sales Records.csv')

# printing names of all columns
print(dataset.columns.values)

# printing 10 rows and columns
print(dataset.iloc[:10,:10])

# plot graphh to represent total profit
tprofit = dataset['Total Profit']
plt.plot(tprofit)
plt.xlabel('unit')
plt.ylabel('total profit')

# item types having profit more than 1000000
itm = dataset['Item Type']
for i in range(len(tprofit)):
    if tprofit[i] > 1000000 :
        print(i,':',itm[i])