# Write a Python program to create and display all combinatons of letters,
# selectng each leter from a different key in a dictonary

'''sample data:{'1':['a','b'],'2':['c','d']}
expected output:ac,ad,bc,bd'''

d1={'101':['A','D'],"102":['E','F']}

lst=list(d1.values())
print(lst)

for x in lst[0]:
    for y in lst[1]:
        print(x+y)


