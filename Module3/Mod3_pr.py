#Write a Python program to read a random line from a file.

import random
fs=open("Test.txt")

print(random.choice(fs.readlines()))

fs.close()