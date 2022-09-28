#Write a Python program to append text to a file and display the text.
#append mode doen not overwrite the file
fs=open("Test.txt","a")
fs.write("\nPython Excercises")
fs.write("\nPython Assignments")
fs.close()

fs=open("Test.txt")
print(fs.read())
fs.close()