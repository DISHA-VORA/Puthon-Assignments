# To Find the Highest 3 Values in Dictionary

mydict={"a":100,"d":501,"j":751,"P":1001,"t":251,"m":50}

sorteddict=sorted(mydict.values(),reverse=True)

# print(sorteddict)
print(f"Highest 3 Values:{sorteddict[0:3]}")

# keysWithHighestValue={}
# for key in mydict:
#     if mydict[key] in sorteddict[0:3]:
#            keysWithHighestValue[key]=mydict[key]

KeyValWithHighetseValue={}
for val in sorteddict[0:3]:
    for key1,val1 in mydict.items():
        if val1==val:
            KeyValWithHighetseValue[key1]=val1

    # if val in mydict.values():
    #     pass
    #         # keysWithHighestValue[key]=mydict[key]

# print(keysWithHighestValue) #kEY Order Sorting is pending yet
print(KeyValWithHighetseValue)