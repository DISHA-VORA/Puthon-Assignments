# Checking if Even Number / Odd Number
num=int(input("Enter The Number for Checking of Even/Odd: "))
res=num%2

if res==0:
    print(f"Number {num} is even")
else:
    print(f"Number {num} is Odd")
