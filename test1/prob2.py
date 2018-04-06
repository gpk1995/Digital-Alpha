# Prob 2
tu = ()
lis = []
for i in range(0, 2):
    name = input("Enter the name ")
    sub1 = int(input("Enter the sub1 mark "))
    sub2 = int(input("Enter the sub2 mark "))
    sub3 = int(input("Enter the sub3 mark "))
    add = sub1+sub2+sub3
    tu = (name, sub1, sub2, sub3, add)
    lis.append(tu)
    
print("Marks")
for i in range(len(lis)):
    print(lis[i][1], "\t", lis[i][2], "\t" + lis[i][2])