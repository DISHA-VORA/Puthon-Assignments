#Remove an Empty tuple from a list of tuple
tuplst=[(58,75),(),(101,601,75,141),(),(899)]
print(f"Original Tuple's List:{tuplst}")

ind=0
for item in tuplst:
    if len(item)==0:
        tuplst.pop(ind)
    ind+=1
# tuplst.pop() without arguments remove last element
print(f"After Removing Blank Tuple from List{tuplst}")