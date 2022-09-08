# Write a Python program to combine values in python list of dictonaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
# 300},{'item': 'item1', 'amount': 750}]
# o Expected Output: Counter ({'item1': 1150, 'item2': 300})
from collections import Counter
dct1=[{'item':'item1','amount':400},{'item':'item2','amount':300},
{'item':'item1','amount':750}]

newdct={}
result=Counter()

for item in dct1:
    result[item['item']]+=item['amount']
    key1=item['item']
    val1=item['amount']
    if key1 in newdct:
        newdct[key1]+=val1
    else:
        newdct[key1]=val1

print(result)
print(newdct)



