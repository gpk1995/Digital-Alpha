from numpy import *
a = ([['Rhia',10,20,30,40,50],
['Alan',75,80,75,85,100],
['Smith',80,80,80,90,95]])

# Slicing the matrix
b = array(a)
b[0:3, 0:2].tolist()

# updating 3rd row
a[2] = ['Sam',82,79,88,97,99]

# updating 4th element of 1st row by 95
a[0][4] = 95

# adding a new column in this matrix with the following values, 73, 80 and 85
c = np.insert(c, 6, (73,80,85),axis=1)