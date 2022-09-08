#Write a python script to merge two dictionary
dict1={"Mon":11,"Tue":15}
dict2={"Wed":25,"Fri":27,"Mon":28}

print(f"Dict1: {dict1}")
print(f"Dict2: {dict2}")
dict1.update(dict2)
print(dict1)