# Check whethte a list contains a sublist

from operator import truediv


list1=["Mon","Tue","wed","Thr","fri",["Sat","sun"]]
print(list1)
flag=False
for item in list1:
    if type(item)==type(list1):
        print("List Contain a sublist")
        flag=True
        break

if flag==False:
    print("List does not contain a sublist")    

#check sublist exists in list or not
list1=["Mon","Tue","wed","Thr","fri"]
list2=["wed","fri"]

if set(list2).issubset(list1):
    print("Using Subset List2 is Part of List1")
else:
    print("Using Subset List2 is not part of List1")

if set(list1).intersection(list2)==set(list2):
    print("Using Intersection Sublist is part of Main List")
else:
    print("Using Intersection Sublist is not part of Main List")

#Pending to clear all and inner syntax
if all(x in list1 for x in list2):
    print("Using All Sublist is part of Main List")
else:
    print("Using all Sublist is not part of Main List")

#AS Per Session Discussion in this way item must be serialize
# list2=["wed","Thr"]
flag=False
for i in range(len(list1)-len(list2)+1):
    if list1[i:i+len(list2)]==list2:
        flag=True
        break

if flag:
    print("Using Session Discussion Sublist is part of Main List")
else:   
    print("Using Session Discussion Sublist is not part of Main List")

def checkListcCntainsSubList(list1,list2):
    flag=False
    if list2==list1:
        flag=True
    elif len(list2)>len(list1):
        flag=False
    else:
        cn=0
        for i in range(len(list1)):
            if list1[i]==list2[0]:
                cn=1
                while (cn<len(list2) and list1[i+cn]==list2[cn]):
                    cn+=1
                    if cn==len(list2):
                        flag=True
                        break
                        
    if flag==True:
        print("Using Function List1 is part of List2")
    else:
        print("Using Function List1 is not part of List2")

checkListcCntainsSubList(list1,list2)