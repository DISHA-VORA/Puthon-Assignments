#sort dictionary by value in asc/dec form

dct={"India":44,"Australia":201,"Canada":178,"Nepal":38}
print(f"Original dictionary:{dct}")

lst=list(dct.values())
lst.sort()
# lst.sort(reverse=True)#decending
print(lst)

srtdct=sorted(dct.items(),key=lambda x:x[1])

print(f"Original dictionary:{dct} asc Sorted Dictionary:{srtdct}" )

srtdct=sorted(dct.items(),key=lambda x:x[1],reverse=True)

print(f"Original dictionary:{dct} dec Sorted Dictionary:{srtdct}" )

sortdict=sorted(dct.values())

# print(sortdict)
newdict={}
for k in sortdict:
    for item,val in dct.items():
        # newdict(dct.get())
        if val==k:
            newdict[item]=val

print(newdict)


