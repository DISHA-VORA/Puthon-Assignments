# Write a Python function that checks whether a passed string is palindrome or not
#palindrome means thar reads same as backword and forward
strtmp="MADAM"

def chkPalindrome(strtmp):
    strtmpreverse=strtmp[::-1]
# print(strtmpreverse)
    if strtmp==strtmpreverse:
        print(f"Given String {strtmp} is palindrome string")
    else:
        print(f"Given String {strtmp} is not palindrome string")

chkPalindrome(strtmp)
