# Prob 4
name = []
age = []
children = []
youth = []
middle = []
senior = []
for i in range(0,20):
    name.append(input("Enter the names "))
    age.append(int(input("Enter the names ")))
    
for i in range(0,20):
    if age[i] in range(0,9):
        children.append(name[i])
    elif age[i] in range(10,30):
        youth.append(name[i])
    elif age[i] in range(31,50):
        middle.append(name[i])
    else:
        senior.append(name[i])

print("People belong to children group", children)
print("People belong to youth group", youth)
print("People belong to middle aged group", middle)
print("People belong to senior group", senior)