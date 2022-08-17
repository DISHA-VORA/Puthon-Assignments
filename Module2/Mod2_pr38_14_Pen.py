#sort dictionary by value in asc/dec form

dct={"India":44,"Australia":201,"Canada":178,"Nepal":38}
print(f"Original dictionary:{dct}")

lst=list(dct.values())
lst.sort()
# lst.sort(reverse=True)#decending
print(lst)

