# Calculate Fibonacci Series
# Next number is sum of two previous Number

num=int(input("Enter a Number to Calculate Fibonnaci Series:"))

srCalc=0
n1=0
n2=1

for i in range(1,num+1):
    if i==1:
        srCalc=n1+n2
        print(n1)
        print(n2)
        print(srCalc)
    else:
        n1=n2
        n2=srCalc
        srCalc=n1+n2
        print(srCalc)


