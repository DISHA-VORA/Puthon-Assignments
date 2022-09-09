# Calculate Fibonacci Series
# Next number is sum of two previous Number

from itertools import count
from tkinter import Y
from typing import Counter


num=int(input("Enter a Number to Calculate Fibonnaci Series:"))

srCalc=0
n1=0
n2=1

for i in range(1,num-1):
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

#Session Discussion Logic
n1=0 #start
n2=1 #base
Counter=0
print("As Per Logic2")
while Counter<num:
    print(n1)
    fib=n1+n2
    n1=n2
    n2=fib
    Counter+=1



