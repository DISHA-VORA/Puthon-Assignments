#What are oops concepts? Is multiple nheritance supported in Python
#Main Ooops charcterictis
# 1> Class - Its a design , blueprint collection of data member(Variable) and member functions
# 2> Object - Its an instance of class. U can assigin diff value to each object. using object u can access class property
# 3> Encapsulation - wrapping of data so u can not access class property outside the class without creation an object
# 4>Inheritance - Its a master-child relationship. using this u can access super class property. so u can share one class property to another class
    # Singal Inheritance,Multiple Inhertiance,Multi level Inheritance
# 5>Polymerphism - One name diff forms.
    # -Method Overloading - In same class same method name comes more than one time but diff arguments of each method
    # -Method Overriding - Class is diff same name and same args.. this is used in inheritance
# 6>Access Specifier - Public and private. by default everything is public . u can mark it private using (double underscore)

# Yes Multiple Inhertiance is supported in Python

class ClassTest:
    stid=101
    stNm="Test" #Class Variable If the value of a variable is not changing from object to object, such types of variables are called static variables or class level variables

    def __init__(self):#Construcor called automatically when instance is created use for initilazation
        self.city="Morbi" #f the value of a variable is changing from object to object then such variables are called as instance variables
        self.Branch="SanalaRoad"

    def getData(self):
        print(self.Branch)
        print(self.city)
        a=10 #local variable
        print(a)



st=ClassTest()
print(st.stid)
print(st.stNm)
print(st.printData())