#write a function that takes list of words and returns the length of longest one
def wordLen(words):
    maxlen=0
    for word in words:
        if maxlen<len(word):
            maxlen=len(word)
    return maxlen

words=["Jain","Sangini","JIO"]

maxlen=wordLen(words)

print(f"Current List {words} and Length of Longest one: {maxlen}")

