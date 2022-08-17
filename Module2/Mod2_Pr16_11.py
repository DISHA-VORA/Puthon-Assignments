"""print a list of first and last 5
elements where the values are square of numbers between 1 and 30."""

def printlstsqrt(num1,num2):
    list1=[]
    for i in range(num1,num2+1):
         list1.append(i*i)
    print(list1[:5]) #First 5 elements
    print(list1[-5:]) #last 5 Elements

printlstsqrt(1,30)