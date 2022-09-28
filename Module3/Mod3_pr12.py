#Write a Python program to write a list to a file.
lst=["Jan","feb","March","april"]
with open("TestList.txt","w") as fs:
    # fs.writelines(lst) #comes as singal line 
    newlist=["{}\n".format(item) for item in lst]
    # fs.write("\n")
    # fs.write("\n")
    fs.writelines(newlist)
    fs.write("\n")
    
    for item in lst:
        fs.write("%s\n"%item)

    # fs.write("\n")
    # fs.write("Using Map")
    # map(lambda item:print(item),lst) #dis pending using map


