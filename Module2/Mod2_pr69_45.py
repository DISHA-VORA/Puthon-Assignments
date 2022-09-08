# How to calculate surface volume and area  of a cylinder
# cylinder = 2πr(r + h)
# where r--> radious of base circle and  h is the height of the curve surface.

# Volume of cylinder=πr²h
# where r--> radious of base circle and h is the height of the curve surface.
import math
r=float(input("Enter radius of a cylindar:"))
h=float(input("Enter Hiight of a cylindar: "))

# area=2*math.pi*r*r*h
area1=2*math.pi*pow(r,2)*h

# print(area)
print("Area of a cylindar:%.2f" %area1)

volume=math.pi*pow(r,2)*h

print("Volume of a cylindar:%.2f" %volume)