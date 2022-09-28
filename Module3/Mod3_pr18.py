#When is the finally block executed
#Finally Block executes every time either error occurs or not

try:
    pass
except Exception as error:
    print(error)
finally:
    print("Finally Block exectues every time")