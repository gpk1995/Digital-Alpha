lower = 1
upper = 1000

for arm in range(lower, upper + 1):
    p = len(str(arm))
    
    sum = 0
    
    alt = arm
    while alt > 0:
        dig = alt % 10
        sum += dig ** p
        alt = alt//10
        
    if arm == sum:
        print(arm)