#Write a Program to Convert Tuple to a string
tup="Mon","Tue","Sat",50

def converttupTostr(tup):
    tmpstr=""
    for item in tup:
        tmpstr+=str(item)
    print(tmpstr)


converttupTostr(tup)