# Write a Python func􀆟on to check whether a number is perfect or not
# a perfect number is sum of its positive divisor excluding number itself
# a perfect number is a number that is half the sum of all of its positive divisors (including itself).
# Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. 
# Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6.
#  The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128
num=8

tmpsum=0
for i in range(1,num):
    if (num%i)==0:
        tmpsum+=i

if(tmpsum==num):
    print(f"{num} is perfect number")
else:
    print(f"{num} is not perfect number")