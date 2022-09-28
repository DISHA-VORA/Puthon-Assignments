# How Do You Handle Exceptions With Try/Except/Finally In Python?
# Explain with coding snippets

# The code which can raise an error is placed inside try block
# The code that handles the exception is written in the except clause
def div(x,y):
    try:
        result=x/y
    except Exception as e:
        print(e)
    #Handling of exception
    #Optional Block
    else:
        # execute if no exception
        print("Your Result:",result)
    finally:
        #always executed
        print("Always Execute")

div(5,2)
div(5,0)


