#How do you Perform a pattern matching ?explain
# Pattern Matching is used in Validation ,Regular Expression

import re
mystr="Hello Students! Welcome to the Class of Python"

x=re.match("Students",mystr)#Return Object with Position Nono as output pending check
print(x)

x=re.search('Welcome',mystr)
print(x)

x=re.findall('the Class',mystr)#return List
print(x)


