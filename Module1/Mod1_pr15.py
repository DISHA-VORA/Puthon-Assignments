#occurances if each word in given sentence

tmpStr="This is Python Programming Python is Everywhere."
splitedstr=tmpStr.split() #Splited by spaces 

print(tmpStr)
print("")
for i in range(0,len(splitedstr)):
    countstr= tmpStr.count(splitedstr[i])
    if countstr>1 and i>0:
        blnfnd=False
        for j in range(0,i):
            if splitedstr[j]==splitedstr[i]:
                blnfnd=True
                break
        if blnfnd==False:
            print(f"{splitedstr[i]} - {countstr}")     
    else:
        print(f"{splitedstr[i]} - {countstr}")
