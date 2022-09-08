#Write a function that returns largest number,smallest number,and sum of all from the list
def listfnd(lstTemp):
    minlist=min(lstTemp)
    maxlist=max(lstTemp)
    sumlist=sum(lstTemp)
    lstRes=[]
    lstRes.extend([minlist,maxlist,sumlist])
    return lstRes


list1=[501,251,751,1151,5000,150,50]
lstRes=listfnd(list1)
print(f"Original List{list1} ,Smallest No:{lstRes[0]},Highest No:{lstRes[1]}, Sum of all:{lstRes[2]}")

# res=list1[0]

# for i in list1:
#     if i<res:
#         res=i

# print(res)

# list1.sort()
# mininumval=list1[0]
# maxval=list1[-1]
