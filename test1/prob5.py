# Prob 5
import numpy as np
from collections import Counter
X = [11.95, 11.91, 11.86, 11.84, 12.00, 11.93, 12.00, 11.94]
Y = [12.10, 11.95, 11.99, 11.94, 11.89, 12.01, 11.99, 11.94]
A = [11.95, 11.91, 11.86, 11.84, 12.00, 11.93, 12.00, 11.94, 12.10, 11.95, 11.99, 11.94, 11.89, 12.01, 11.99, 11.94 ]


# frequency distribution
fd = Counter(A)
print("frequency distribution", fd)

# mean, median, mode
mean = np.mean(A)
median = np.median(A)
mode = Counter(A).most_common()[0]
print(mean)
print(median)
print(mode)