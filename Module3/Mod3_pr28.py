#What is used to check whether an object o is an instance of class A?

#Using isinstance() we can test whether an object/variable is an instance of specific class such as list,int

class A:
    def __init__(self):
        print("This is class A")

class B:
    def __init__(self):
        print("This is class B")
a=B()
if isinstance(a,A):
    print("Yes a is instance of Class A")
else:
    print("No, a is instance of Class B")

