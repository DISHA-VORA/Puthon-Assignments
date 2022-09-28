#Write python program that user to enter only odd numbers, else will raise an excepton.
try:
    num=int(input("Enter a number:"))
    if not num%2==0:
        raise ValueError("Please Enter Odd Number")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(e)
else:
    print("No Exception")
