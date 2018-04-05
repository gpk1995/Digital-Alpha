lower = 900
upper = 1000

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   if num > 1:
       for i in range(2,int(num/2)):
           if (num % i) == 0:
               break
       else:
           print(num)
           if num%10 == 9:
               print(num ,"is a palindrome")