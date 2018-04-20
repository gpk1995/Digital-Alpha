import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn import datasets
from sklearn.metrics import confusion_matrix

# data preprocessing
data = pd.read_csv("income.csv")
data = data.dropna()
le = LabelEncoder()
data['Income (Rs)'] = le.fit_transform(data['Income (Rs)'])

# creating dummy variables of categorical variables
data1=pd.get_dummies(data,columns=['Employment','Marital Status', 'Gender'])

data1_final_vars = data1.columns.values.tolist()
y=['Income (Rs)']
X=[i for i in data1_final_vars if i not in y]

print(X)

# RFE
logreg = LogisticRegression()

rfe = RFE(logreg, 5)
rfe = rfe.fit(data1[X], data1[y])
print(rfe.support_)
print(rfe.ranking_)


cols=['Employment_Govt', 'Employment_Private', 'Employment_Self Employed', 'Marital Status_single', 'Gender_M']

# final data
X=data1[:10][cols]
y=data1[:10]['Income (Rs)']

# Fitting the dataset to logreg model
logreg = LogisticRegression()
logreg.fit(X, y)

# testint the model
X_test = data1[10:12][cols]
y_pred = logreg.predict(X_test)