#split list to a diff variable

list1=["Jan","May","July","Oct"]
cnt=0
acnt=0
var1,var2,var3,var4=list1
print(var1)
print(var2)
print(var3)
print(var4)

print("\nUsing Arbitary Arguments")
def splitlst(* lstvars):
    # print(lstvars[0])
    for i in range(0,len(lstvars)):
            print(lstvars[i])

splitlst(*list1)

