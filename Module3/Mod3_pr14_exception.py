#Explain Excepton handling? What is an Error in Python?
# Exception:Synatiacally Statement is correct even though at run time an error has come when that statemnt is excutet is called excdeption
# Error: When statement is not accordance with prescribed statement

#Exception sample

a=58
b=0

try:
    print(a/b)
except Exception  as e:
    print("Error:", e)

# Error Sample Visual code editior immediately shown as error it cannot allow u to run the code
# print(a*B)
