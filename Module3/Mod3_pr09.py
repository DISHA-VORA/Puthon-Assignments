#Write a python Program to find the longest words
from audioop import reverse


def find_longestWordsfromFile(filename):
    with open(filename) as fs:
        words=fs.read().split()
        # words.sort() #Capitalization issue has come
        # print(words[0])

        s=sorted(words,key=len)
        print(s[-1])

        maxlen=len(max(words,key=len))
        longestword=""
        for word in words:
            if len(word)==maxlen:
                longestword=word
                break
        print(longestword)


find_longestWordsfromFile("Test.txt")
