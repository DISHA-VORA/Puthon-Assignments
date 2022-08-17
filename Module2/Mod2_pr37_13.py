#How will u create a dict using tuple
tup=("Jan","May","July","March")
print(f"Original Tuple:{tup}")
dct={}
ind=1
for item in tup:
    dct["Key"+str(ind)]=item
    ind+=1

print(f"Converted Dictionary:{dct}")