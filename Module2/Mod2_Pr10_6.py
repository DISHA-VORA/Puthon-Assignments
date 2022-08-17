#Compare Two Lists
list1=[35,57,89]
list2=[57,89,35]

if list1==list2:
    print("Lists are Equal")
else:
    print("Lists are not Equal")

    list1.sort()
    list2.sort()

if list1==list2:
    print("After Sorting Lists are Equal")
else:
    print("After Sorting Lists are not Equal")