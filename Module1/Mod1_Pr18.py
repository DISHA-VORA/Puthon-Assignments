# Find first appearance of the substring 'not' and 'poor' from a given string
# if 'not' follows the 'poor' ,replace the whole 'not' ..'poor' substring 'good'
# return result string

tmpstr="Sam is not poor"

findPos1=tmpstr.find("not")
findpos2=tmpstr.find("poor")

newstr=""

# print(findPos1)
# print(findpos2)
# print(tmpstr.find("not poor"))

if findPos1>0 and findpos2>0:
    if findPos1<findpos2 and tmpstr.find("not poor")>0:
        newstr=tmpstr.replace("not poor","good")
    else:
        newstr=tmpstr    
else:
    newstr=tmpstr

print(f"Old String: {tmpstr} Converted String: {newstr}")

