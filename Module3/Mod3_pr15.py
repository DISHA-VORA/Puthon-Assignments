#How many except statements can a try-except block have? Name Some
# built-in excep􀆟on classes

#It can be at least one or many Except clause in try except block

num1,num2=8,0

try:
    # print(num1/num2)
    print('83'+ num1)
except ZeroDivisionError as e1:
    print("Divide By Zero Exception:-" + str(e1))
except Exception as e:
    print("Incompitable Type:-" + str(e))
finally:
    print("Finally Block always Executes")

