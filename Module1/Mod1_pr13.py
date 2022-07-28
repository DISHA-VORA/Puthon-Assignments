#Use of Negative Indexes and why are they used
#Negative indexs starts from End . so -1 means last element,-2 means second last and so on
#use of it to check ending character/string like space,comma,dot..so on

tmpstr="Hello World!"
strlen=len(tmpstr)

for i in range(1,strlen+1):
    print(tmpstr[-i])


