str1 = input("Enter a sentence ")

l = len(str1)

lc = 0
ac = 0
for i in range(0, l):
    if str1[i].isnumeric():
        lc += 1
    elif str1[i].isalpha():
        ac += 1
        
print("Number of letters in the sentence", ac)
print("Number of digits in the sentence", lc)