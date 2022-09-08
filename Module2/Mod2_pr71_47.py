#Write a Python program to find the maximum and minimum numbers
# from the specified decimal numbers.

# lst=[2.45,7.5,3.5,8.5,9.5,1.54,1.53]
# mindata=min(lst)
# maxdata=max(lst)

# print("Given List")
# print(f"Minimum Number{mindata}")
# print(f"Maximum Number{maxdata}")

from decimal import *
data = '2.45 2.69 2.45 3.45 2.00 0.04 7.25'.split()
print(min(data))
print(max(data))