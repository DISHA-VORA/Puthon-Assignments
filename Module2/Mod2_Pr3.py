# get a string made of a given string's first 2 and last 2 chars.if string<2 then return empty string  
def creStr(tmpstr):
    strlen=len(tmpstr)
    newstr=""
    if strlen<2:
        newstr=""
    elif strlen==2:
        newstr= tmpstr+tmpstr 
    else:
        newstr=  tmpstr[0:2] + tmpstr[-2:]
    return newstr
tmpstr=input("Enter a String: ")
newstr=creStr(tmpstr)

print(f"Given String: {tmpstr}  and new String: {newstr}")
