# Explain Inheritance in Python with an example? What is init? Or What Is
# A Constructor In Python

#Inheritance is master-child relationship. its a mechanism to inheriting the properties of the base class to the child class
#Constructor is special method which calls automatically when instance is created.
#task of constructor is to initialize variable to the data memeber of class
#__init__() is a constuctor
#Every class in inherited from a built in class called 'object'
#Python supports three types of inheritance singal lebel,multi level and multiple inheritance

class grandMa:
    def __init__(self,grandmanm):
        self.gmNm=grandmanm

class Mother(grandMa):
    def __init__(self, grandmanm,MotherNM):
        self.motherNM=MotherNM
        super().__init__(grandmanm)

M=Mother("Lilamben","Pushpaben")
print(f"GrandMA:{M.gmNm}")
print(f"Mother:{M.motherNM}")

