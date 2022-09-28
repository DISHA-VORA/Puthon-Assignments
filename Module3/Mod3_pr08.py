# Write a Python program to read a file line by line store it into a variable
def read_file(filename):
    with open(filename) as fs:
        cnt=1
        while True:
            line=fs.readline()
            if not line:
                break
            print(f"Line {cnt}:{line}")
            cnt+=1

read_file("Test.txt")
