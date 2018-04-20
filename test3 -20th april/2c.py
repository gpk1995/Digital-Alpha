import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# data preprocessing
data = pd.read_csv("income.csv")
data = data.dropna()
le = LabelEncoder()
data['Income (Rs)'] = le.fit_transform(data['Income (Rs)'])
X = np.array(data.iloc[:10, :-1].values).reshape(-1, 4)
y = np.array(data.iloc[:10, -1].values).reshape(-1, 1)

cluster_count = 2

cluster1_centroid = X.random.randInt

def euclidean_distance(2, X, y):
    for i in 