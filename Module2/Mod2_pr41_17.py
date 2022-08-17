#Traverse through a dictionary object
stdict={"id":"101","Name":"Test","Sub":"Python"}
#statesAndCapitals = {
#     'Gujarat': 'Gandhinagar',
#     'Maharashtra': 'Mumbai',
#     'Rajasthan': 'Jaipur',
#     'Bihar': 'Patna'
# }
print("Keys:")
for item in stdict:
    print(item)

print("\nValues:")
for item in stdict.values():
    print(item)

print("\nKeys And Values:")
for k,v in stdict.items():
    print(f"Key={k} and Value={v}")