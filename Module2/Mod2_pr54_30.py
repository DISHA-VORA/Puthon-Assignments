#write a function to calculate factorial of a given number
import math
def fact(num):
    if num==1 or num==0:
        return 1
    return num*fact(num-1)

def fact2(num):
    product=1
    for n in range(1,num+1):
        product*=(n)
    return product

print(fact(5))
print(fact2(5))
print(math.factorial(5))