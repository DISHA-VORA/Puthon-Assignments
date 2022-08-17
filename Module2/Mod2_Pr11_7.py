#from a given string list count no of strings where length>=2 and first and last chars are same
strlist=["Alka","Mira","Rajvir","Param","Tatva","A","dD"]
noofStr=0
for str in strlist:
    if len(str)>=2:
        if str[0].upper()==str[-1].upper():
            noofStr+=1

print(f"Original List: {strlist} And no Of String whose Length>=2 and First and Last chars are equal: {noofStr}")


