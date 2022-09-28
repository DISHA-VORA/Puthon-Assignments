# Write a Python program to count the number of lines in a text file
def cntNoofLinesFromFile(filename):
    with open(filename) as fs:
       noofline=len(fs.readlines())

    print(f"No of lines in file:{noofline}")

    with open(filename) as fs:
        for count,line in enumerate(fs):
            # print(count,line)
            pass
        
    print(f"No of lines in file Using Enumerate Method:{count+1}")

cntNoofLinesFromFile("Test.txt")