# Write a Python program to create a dic􀆟onary from a string.
# Track the count of the leters from the string. Sample string:
# 'w3resource'
# o Expected output: {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

from collections import Counter


tmpstr="w3resource"
mydict={}
result=Counter(tmpstr)
print(result)

for letter in tmpstr:
    mydict[letter]=mydict.get(letter,0)+1#check dict get method

print(mydict)