#Write a Python program to read last n lines of a file
fs=open("Test.txt")

lastnooflines=4

lstlines=fs.readlines()

for strline in lstlines[-lastnooflines:]:
    print(strline)

fs.close()
