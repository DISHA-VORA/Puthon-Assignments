#Write a Python class named Rectangle constructed by a length and width
# and a method which will compute the area of a rectangle

class Rectangle:
    def __init__(self,l,w):
        self.length=l
        self.width=w

    def rect_area(self):
        return self.length*self.width

r=Rectangle(12,10)
print(r.rect_area())
