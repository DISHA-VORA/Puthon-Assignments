#SWapt Two numbers with and witout Temp Number
num1=int(input("Enter a number1: "))
num2=int(input("Enter a number2: "))

orgnum1,orgnum2=num1,num2

#With temp Variable
tempnum=num1
num1=num2
num2=tempnum

print("")
print(f"Original Num1 : {orgnum1} Num2:{orgnum2}")
print(f"After Swapping With Temp num1:{num1}")
print(f"After Swapping With Temp num2:{num2}")

num1,num2=orgnum1,orgnum2

#Withut Temp Variable
num1,num2=num2,num1
print("")
print(f"Original Num1 : {orgnum1} Num2:{orgnum2}")
print(f"After Swapping Without Temp num1: {num1}")
print(f"After Swapping Without Temp num2: {num2}")

#Third Way
num1,num2=orgnum1,orgnum2

num1=num1+num2 # same using *,^
num2=num1-num2 # same using /,^
num1=num1-num2 # same using /,^

print("")
print(f"Original Num1 : {orgnum1} Num2:{orgnum2}")
print(f"After Swapping With Add/Sub num1: {num1}")
print(f"After Swapping With Add/Sub num2: {num2}")


