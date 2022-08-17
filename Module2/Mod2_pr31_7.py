#reverse tuple
#There is no method reverse in tuple so either u can use slicing or first convert it to list amd than reverse and again convert to tuple

tup=("I","N","D","I","A")
# lst=["ind","afr"]
x=(list(tup))
x.reverse()
z=reversed(tup)
# lst.reverse()
print(tuple(x))
# print(lst)
print(tup[::-1])
print(tuple(z))

