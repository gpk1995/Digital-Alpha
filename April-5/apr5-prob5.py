import math
print("Select the number to perform the operation")
print("1. Factorial 2.LCM 3.HCF 4. Factor of a number")

choice = int(input("Enter you choice "))


if choice == 1:
    num = int(input("Enter a number "))
    print("Factorial of %s is %s" %(num, math.factorial(num)))
    
elif choice == 2:
    a = int(input("Enter 1st number "))
    b = int(input("Enter 2nd number "))
    print("LCM of %s and %s is %s" %(a, b, ((a*b)/math.gcd(a, b))))
    
elif choice == 3:
    a = int(input("Enter 1st number "))
    b = int(input("Enter 2nd number "))
    print("HCF of %s and %s is %s" %(a, b, math.gcd(a, b)))
    
else:
    x = int(input("Enter a number "))
    print("Factor of %s is" %(x))
    for i in range(1, int(x/2) +1):
        if(x % i == 0):
            print(i)