#write  a function that reverse string if length of string is multiple of 4

def revStr(tmpstr):
    if (len(tmpstr)%4)==0:
       return tmpstr[::-1]  #Reverse the string
    else:
        return tmpstr 

tmpstr="World Wide Web"
for word in tmpstr.split():
    newstr=revStr(word)
    print(word + "-" + newstr)


