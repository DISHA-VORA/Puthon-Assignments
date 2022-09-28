#How to Define a Class in Python? What Is Self? Give An Example Of A Python Class
# self represents the class itself . is a reference to the current instance of the class and is used to access variables that belong to the class

class A:
    a=10

    def __init__(self):
        print(self.a) #accessing static/class variable
        print(A.a) #accessing static/class variable
        self.branch="Rajkot" #Instance variable
        print(self.branch)

a=A()
