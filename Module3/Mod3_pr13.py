# Write a Python program to copy the contents of a file to another file
from shutil import copyfile
with open("test.txt") as fr,open("TestCopy.txt","w") as fw:
    for line in fr:
        fw.write(line)

copyfile("test.txt","TestCopy2.txt")