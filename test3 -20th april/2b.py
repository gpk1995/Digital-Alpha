import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

# data preprocessing
data = pd.read_csv("income.csv")
data = data.dropna()
data1 = data

# Label encoding
le = LabelEncoder()
data1['Income (Rs)'] = le.fit_transform(data1['Income (Rs)'])
data1['Employment'] = le.fit_transform(data1['Employment'])
data1['Marital Status'] = le.fit_transform(data1['Marital Status'])
data1['Gender'] = le.fit_transform(data1['Gender'])

# Slicing
X = data1.values[:10, :-1]
y = data1.values[:10, -1]

# Fitting Gaussian Naive Bayse
nbc = GaussianNB()
nbc.fit(X, y)

# testing the model
X_test = data1.values[10:12, :-1]
y_pred = nbc.predict(X_test)