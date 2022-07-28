# add ing at the end of a given string (Length should be at least 3) 
# if given string ends with 'ing' then add 'ly' 
# if giben string length is less than 3 leave it unchanged

tmpstr=input("Enter a string : ")
newstr=""

if len(tmpstr)<=3: 
    newstr=tmpstr
elif tmpstr.endswith("ing"):
    newstr=tmpstr + "ly"
else:
    newstr=tmpstr+'ing'

print(f"Original String: {tmpstr} \t new String: {newstr}")

