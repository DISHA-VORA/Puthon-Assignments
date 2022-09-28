#Write a Python Program to read an Entire File text file
fs=open("Test.txt","r")
for x in fs:
    print(x)

print(fs.read())

print(fs.readline())
fs.close()