#insert string in the middle of a string
strTemp="w3.com"
insertedStr="Schools"

newstr=strTemp[0:2]+insertedStr+strTemp[2:]

print(f"Original string: {strTemp} inserted String:{insertedStr} and new string:{newstr}")