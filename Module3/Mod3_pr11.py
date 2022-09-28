#Write a Python program to count the frequency of words in a file
from itertools import count
from typing import Counter


with open("Test.txt") as fs:
   words=fs.read().split()

wordcnt={}
for word in words:
    if not word in wordcnt:
        wordcnt[word]=words.count(word)

print(wordcnt)

print(Counter(words))