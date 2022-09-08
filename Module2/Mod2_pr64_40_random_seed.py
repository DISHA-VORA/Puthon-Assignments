# how will u set the starting number in generating random number
#the generator creates a random number based on the seed value, so if the seed value is 10, you will always get 0.5714025946899135 as the first random number.

import random

print(random.random()) #Return float every time

print(random.randint(5,10))
random.seed(10)#initialize internal state first random number
print(random.randint(5,10))#This will return same number every time confusing



