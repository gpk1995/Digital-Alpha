import numpy as np
Arr = [0,1,2,3,4,5,6,7,8,9]

A2 = np.array(Arr).reshape(-1,2)

# dimention of the array
print(type(A2))

# updating array to 3 dimensions
C = A2.reshape((A2.shape[0], A2.shape[1], 1))

# adding 5 to every element, subtracting 2 from each element, multiplying each element by 5
C=C+5
C-=2
C*=5