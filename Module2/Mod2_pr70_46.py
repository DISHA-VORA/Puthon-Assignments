#write a python program to return sum of all divisor of a number
num=int(input("Enter a number:"))
def sumofDivisior(num):
    divs=[1]
    for i in range(2,num):
        if num%i==0:
            divs.append(i)
    return sum(divs)

print(sumofDivisior(num))