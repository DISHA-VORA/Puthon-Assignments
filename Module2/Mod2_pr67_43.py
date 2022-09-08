#write a python program to calculate the area of trapezoid
# a=1/2(a+b)h
# area=(a+b)/2*h
base1 = float(input('Please Enter the First Base of a Trapezoid: '))
base2 = float(input('Please Enter the Second Base of a Trapezoid: '))
height = float(input('Please Enter the Height of a Trapezoid: '))

area=0.5*(base1+base2)*height
median=0.5*(base1+base2)

print("\n Area of a Trapezium = %.2f " %area)
print(" Median of a Trapezium = %.2f " %median)

