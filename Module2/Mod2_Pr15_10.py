#Write a function that take two List and return true if at least one member is common

from operator import truediv


list1=["AMD","RJT","MVI","SRT","JMN"]
list2=["GNR","MEH","NMD","AND","MVI"]

def compareList(list1,list2):
    commonMember=False
    for str in list1:
        if str in list2:
             commonMember=True
        if commonMember:
            break
    return commonMember

res=compareList(list1,list2)
print(f"List1:{list1} ,List2:{list2},Common Member:{res}")

           