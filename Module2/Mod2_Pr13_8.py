#Remove dupliate elements from list

list1=[58,85,58,75,85,45,54,75]
newlist=[]
for num in list1:
    if num in newlist:
        pass
    else:
        newlist.append(num)

print(f"Original list{list1} and after removing Duplicate:{newlist}")

#Another Way
newlist.clear()
newlist=list(dict.fromkeys(list1))
print(f"Another Way Original list{list1} and after removing Duplicate:{newlist}")