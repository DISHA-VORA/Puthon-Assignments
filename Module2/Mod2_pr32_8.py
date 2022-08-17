#program to replace last value of tuples in a list.
# tup=("GJ36","GJ03","GJ32","GJ18")1
# print(tup)
# x=list(tup)
# x[-1]="GJ25"
# print(tuple(x))
# tup=([11,21,31],[101,201,301],[1101,1201,1301])

lst = [(101, 201, 401), (401, 501, 601), (701, 801, 901)]
# print([t[:-1] + (100,) for t in lst])
tmpstr="["
for t in lst:
    tmpstr+=str((t[:-1] + (100,) ))
    tmpstr+=","
tmpstr=tmpstr[:-1]
tmpstr+="]"
print(tmpstr)