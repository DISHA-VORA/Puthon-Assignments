#When will the else part of try-except-else be executed
#Else file executes only sucessful completion of try block means when there is no error


try:
    # print("15"+15)
    print(15+15)
except Exception as e:
    print(e)
else:
    print("On Sucessful Completion of try Block else Block Executes")
finally:
    print("Finally Block Always Execute though Exception is generated")



