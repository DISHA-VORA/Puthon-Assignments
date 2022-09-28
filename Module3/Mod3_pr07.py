# Write a Python program to read a file line by line and store it into a list
def file_read(filename):
    cnt=1
    with open(filename) as fs:
        for line in fs:
            # linelst=fs.readline()
            print(f"Line {cnt} :{line}")
            cnt+=1

    with open(filename) as fs:
        linelist=fs.readlines()
    
    cnt=1
    for line in linelist:
        print(f"Line {cnt} :{line}")
        cnt+=1

file_read("Test.txt")