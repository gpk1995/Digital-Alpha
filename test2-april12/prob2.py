import numpy as np
import pandas as pd
import csv

l = {} 
with open('students.csv', 'w') as csvfile:
    fieldnames = ['name', 'age', 'gender', 'height', 'weight']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    for i in range(0, 5):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        gender = input("Enter gender: ")
        height = int(input("Enter height: "))
        weight = int(input("Enter weight: "))
        l = {'name': name, 'age' : age, 'gender' : gender, 'height' : height, 'weight': weight}
        writer.writerow(l)
        
        
dataset = pd.read_csv('students.csv')   
        