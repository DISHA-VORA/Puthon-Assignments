# how will u randomize the items of a list in place?
import random

lst=["abc","dj","td","at","pnv","dnv","nis"]

print(random.choice(lst))
random.shuffle(lst)
print(lst)