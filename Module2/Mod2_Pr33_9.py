#find the repeated items of a tuple
from operator import indexOf


tup=(58,75,25,75,21,25,21)
s=set(tup)
lstdup=[]
unqItems=[]

if len(tup)==len(s):
    print("No Duplicate Items")
else:
    ind=0
    for item in tup:
        # tup.index(item)
        pos= indexOf(tup,item)
        
        if pos!=0 and pos>=ind:
            lstdup.append(item)   
        ind+=1

#Another way use slicing  with in operator upto visited portion of the list
# ind=0
# for item in tup:
#     if ind>0 and item in tup[:ind]:
#         pass
#     else:
#         unqItems.append(item)
#     ind+=1


print(f"Original Tuple{tup} and Repeated Items:{tuple(lstdup)}")
# print(unqItems)