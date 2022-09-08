#write a python program two combine two dictionary adding values for common keys
# d1={'a':300,'b':200,'c':300}
# d2={'a':100,'b':200,'d':400}
# sample output =counter({'a':400,'b':400,'c':300,'d':400})

from typing import Counter


d1={'a':300,'b':200,'c':300}
d2={'a':100,'b':200,'d':400}

print(f"Original Dic1:{d1}")
print(f"Original Dic2:{d2}")

for key in d2:
    if key in d1:
        d1[key]=d1[key]+d2[key]
    else:
        d1[key]=d2[key]

print(f"Merged Dictionary:{d1}")


d1={'a':300,'b':200,'c':300}
d2={'a':100,'b':200,'d':400}

d3=Counter(d1)+Counter(d2)
print(d3)

