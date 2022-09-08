#Write a python program to map two list into a dictionary
lst1=["Mon","Tue","Fri"]
lst2=[25,11,29,30]

dicttmp={}
dicttmp=zip(lst1,lst2) #joining two list as a key/value pair
print(dict(dicttmp))