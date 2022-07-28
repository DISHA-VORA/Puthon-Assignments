#checking if whether character is Vowel or not
letter=input("Please Enter a Character For checking Vowel Or Not: ")
letter=letter.upper()

if letter=='A' or letter=='E' or letter=='I' or letter=='O' or letter=='U':
    print(f"Character {letter} is Vowel")
else:
    print(f"Character {letter} is not Vowel")