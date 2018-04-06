# problem 3
import numpy as np
lis = [12,6,48,37,88,31,54,11,60,122,105,88,122,155,105]
lis.sort()
key = int(input("Enter the value to be searched"))
for i in range(len(lis)):
    if lis[i] == key:
        print("The %s is in index %s" %(key, i))
        break
        
# list of numbers from keybord
def func(n):
    l = []
    for i in range(n):
        l.append(int(input("Enter a number ")))
    
    return l
print("Enter a number(total numbers) to read from keyboard ")
num = int(input())
li = func(num)
print("Entered numbers are", li)