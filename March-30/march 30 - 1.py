import re
str = input("Enter a sentence ")

d=u=l=s=0

for c in str:
    if c.isdigit():
        d += 1
    elif c.isupper():
        u += 1
    elif c.islower():
        l += 1
    else:
        pass

s = sum(bool(re.match(r"""[!.><:;'@#~{}\[\]-_+=£$%^&()?]""", c)) for c in str)

print("Number of letters ", len(str))
print("Number of digits ", d)
print("Number of upper-case letters ", u)
print("Number of lower-case letters ", l)
print("Number of special characters ", s)