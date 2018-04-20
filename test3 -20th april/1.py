import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv("population.csv")

X = np.array(dataset.iloc[:, 0]).reshape(-1, 1) # independent variable
y = np.array(dataset.iloc[:, 1]).reshape(-1, 1) # dependent variable

# fitting the model
regressor = LinearRegression()
regressor.fit(X, y)

# predicting 
y_pred = regressor.predict([[2011], [2021], [2031]])

# visualisation
plt.figure(1)
plt.scatter(X, y)
plt.plot(X, regressor.predict(X), color = 'green')
plt.xlabel('Year')
plt.ylable('Population')
plt.show()