#get Unique Values from a list
list1=["a","b","d","b","a","j"]

unique_lst=[]
for item in list1:
    if item not in unique_lst:
        unique_lst.append(item)

print(f"Original List{list1} Unique List:{unique_lst}")

unqSet=set(list1)
unique_lst.clear()
unique_lst=list(unqSet)
print(f"Using Set Original List{list1} Unique List:{unique_lst}")

