# Write a Python function that takes a list and returns a new list with unique
# elements of the first list.
list1=["Java","C","c++","Python","dotnet","Python","C","Android","Android"]

def uniqueList(list1):
    unqlst=[]
    for lst in list1:
        if lst not in unqlst:
            unqlst.append(lst)
    return unqlst

newlst=uniqueList(list1)
print(f"Original list{list1} new list:{newlst}")



