#Write a Python program to read first n lines of a file
fs=open("Test.txt")

nooflines=3

lstlines=fs.readlines()

for strline in lstlines[:nooflines]:
    print(strline)

fs.close()


