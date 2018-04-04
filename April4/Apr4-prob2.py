import re
stri = "#Python is is an interpreted high level an an programming language for general-purpose programming*."
str1 = re.sub('[^A-Za-z0-9 \-.]+', '', stri)
print(str1)

str2 = stri.split(' ')
for st in str2:
    if(st == st[::-1]):
        print(st)
        

# =============================================================================
# from collections import Counter
# cnt = Counter(str2)
# for val in cnt.values():
#     if(val == 1):
#         pass
#     else:
#         print("%s : %s" %(cnt.keys(),cnt.values())
# =============================================================================

d={}
for i in str2:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
maxi=max(d.values())

for i in d:
    if d[i]>1:
        print(i,":",d[i])