#Write a Python class named Circle constructed by a radius and two
#methods which will compute the area and the perimeter of a circle

import math
from turtle import circle
class Circle:
    def __init__(self,red):
        self.radius=red
    
    def circle_area(self):
        return(math.pi*(self.radius**2))#Power Operator **

    def circle_perimeter(self):
        return(2*math.pi*self.radius)

c=Circle(5)
print(c.circle_area())
print(c.circle_perimeter())