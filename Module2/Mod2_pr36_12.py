#Convert a list of tuples into a dictionary
lsttup=[("Mon","Feb"),("Year","2022"),("Language","Python")]
dictlst={}
print(dict(lsttup))
for item in lsttup:
    key=item[0]
    value=item[1]
    dictlst[key]=value
print(dictlst)