#Write a Python program to convert a list of characters into a string
list=["w","3","r","e","s","o","r","c","e","s"]
strtemp=""
for item in list:
    strtemp+=item

print(f"List:{list} and Converted String:{strtemp}")