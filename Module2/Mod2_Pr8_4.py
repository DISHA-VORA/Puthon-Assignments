#diff between Append() and extend() method
#append method adds singal elment and extends adds  more than one elment or another list also
list1=[24,56,78,98]
print(f"Original List:{list1}")
list1.append(89)
print(f"Appending element to the List:{list1}")
list2=[101,201,201]
list1.extend(list2)
print(f"Extending element to the List:{list1}")
