#unzip a list of tuples into a individual list
# zip(*iterables) takes iterator as an argument and returns an iterator 
# this iterator generates a series of tuples containing elements from each iterable 
#  length of the shortest iterable
# The * operator can be used in conjunction with zip() to unzip the list.

tuplst=[("Jan","Feb"),("Sun","Mon","Sat"),(15,25,35),('a','d','j')]
print(list(zip(*tuplst)))