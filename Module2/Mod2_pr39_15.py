#concatenate dict to create a new dictionary
dict1={"Key1":50,"Key2":85}
dict2={"Key3":101,"Key4":501}
dict3={"Key5":601,"Key6":801}

dict={}
dict.update(dict1)
dict.update(dict2)
dict.update(dict3)
print(f"Dict1:{dict1}")
print(f"Dict2:{dict2}")
print(f"Dict3:{dict3}")
print(dict)