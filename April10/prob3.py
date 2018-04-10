import numpy as np

tup= {}
lis = []

for i in range(0,4):
    name = input("Name of student ")
    subject1 = int(input("Subject 1 mark : "))
    subject2 = int(input("Subject 2 mark : "))
    subject3 = int(input("Subject 3 mark : "))
    subject4 = int(input("Subject 4 mark : "))
    
    total = subject1+subject2+subject3+subject4
    
    tup = {'name':name,'subject1':subject1 ,'subject2':subject2 ,'subject3':subject3 ,'subject4':subject4 ,'total':total }

    lis.append(tup)

print("Name \t Subject1 \t Subject2 \t Subject3 \tSubject4")

# display dictionary containing student data
for i in range(0,len(lis)):
    print(lis[i]['name'],"\t",lis[i]['subject1'],"\t\t",lis[i]['subject2'],"\t\t",lis[i]['subject3'],"\t\t",lis[i]['subject4'])

# highest mark each student
print("\nName \t Max mark")
for i in range(0,len(lis)):
    print(lis[i]['name'],"\t",max(lis[i]['subject1'],lis[i]['subject2'],lis[i]['subject3'],lis[i]['subject4']))
    
# the topper
from operator import itemgetter
l = sorted(lis,key = itemgetter('total'))
l = l[::-1][0]
print("Topper in the class is ")
print("Name \t Subject1 \t Subject2 \t Subject3 \tSubject4 \tTotal")
print(l['name'],"\t",l['subject1'],"\t\t",l['subject2'],"\t\t",l['subject3'],"\t\t",l['subject4'],"\t\t",l['total'])

# marks of all students in ascending order
lt = sorted(lis,key = itemgetter('total'))  
print("Student marks in ascending order")
print("Name \t Subject1 \t Subject2 \t Subject3 \tSubject4")
for i in range(0,len(lt)):
    print(lt[i]['name'],"\t",lt[i]['subject1'],"\t\t",lt[i]['subject2'],"\t\t",lt[i]['subject3'],"\t\t",lt[i]['subject4'])

# marks of first two roll numbers
print("Marks of first two roll numbers")
print("Name \t Subject1 \t Subject2 \t Subject3 \tSubject4")
for i in range(0,2):
    print(lis[i]['name'],"\t",lis[i]['subject1'],"\t\t",lis[i]['subject2'],"\t\t",lis[i]['subject3'],"\t\t",lis[i]['subject4'])


#Add students 5 and 6
for i in range(0,2):
    name = input("Name : ")
    subject1 = int(input("Subject 1 marks : "))
    subject2 = int(input("Subject 2 marks : "))
    subject3 = int(input("Subject 3 marks : "))
    subject4 = int(input("Subject 4 marks : "))
    
    total = subject1+subject2+subject3+subject4
    
    tup = {'name':name,'subject1':subject1 ,'subject2':subject2 ,'subject3':subject3 ,'subject4':subject4 ,'total':total }

    lis.append(tup)
    
print("Name \t Subject1 \t Subject2 \t Subject3 \tSubject4")
for i in range(0,len(lis)):
    print(lis[i]['name'],"\t",lis[i]['subject1'],"\t\t",lis[i]['subject2'],"\t\t",lis[i]['subject3'],"\t\t",lis[i]['subject4'])
