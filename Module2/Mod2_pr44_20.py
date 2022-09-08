#Write a Python program to check multple keys exists in a dictonary
dictstd={"id":101,"name":"test","Class":"I","city":"Rajkot"}

chkkey={"Class","city"}

if dictstd.keys()>=chkkey:
    print("All Keys are present")
else:
    print("All Keys are not present")

# chkkey=set(["id","name1"])

if chkkey.issubset(dictstd.keys()):
    print("All Keys are present")
else:
    print("All Keys are not present")
