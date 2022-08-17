# Check whethte a list contains a sublist
from enum import Flag
from typing import List


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