#Write a python function to check whrther a number is in a given range
num=81
def testrng(n):
    if num in range(5,15):
        print(f"{num} is in range 5 to 15")
    else:
        print(f"{num} is not in range 5 to 15")

testrng(num)