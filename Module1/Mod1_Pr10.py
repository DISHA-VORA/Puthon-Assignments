#Sum of First n Positive integers
# (n*(n+1))/2

num=int(input("Enter a Number For calculation Positive integer:"))
res=0
anotherRes=0
for i in range(1,num+1):
    res+=i
# anotherRes=int((num*(num+1))/2)
print(f"Sum of {num} Positive Integer:{res}")