#factorial of a given Number
#n!=1*2*3...n
num=int(input("Enter a Number for calculating Factorial"))

product=1
for i in range(1,num+1):
    product*=i

print(f"Factorial of a Number{num}={product}")

