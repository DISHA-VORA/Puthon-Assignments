#Sum of three given integers if two values are equal then sum will be 0
num1=int(input("Enter Number1 For Finding Sum: "))
num2=int(input("Enter Number1 For Finding Sum: "))
num3=int(input("Enter Number1 For Finding Sum: "))


if num1==num2 or num1==num3 or num2==num3:
    numsum=0
else:
    numsum=num1+num2+num3

print(f"Sum of Given Number1-{num1},Number2-{num2},Number3-{num3}={numsum}")

