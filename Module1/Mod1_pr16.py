# get a single string from two given string seperated by space and swap first two character of each string

str1="Sam" # "Ahmedabad"
str2= "Jam" # "Memdabad"
newstr=str1+ " " + str2

# using two string
# newstr1 = str2[0:2] + str1[2:]
# newstr2 = str1[0:2] + str2[2:]

#using singal string
findPos=newstr.find(" ")

newstr1=newstr[findPos+1:findPos+3] + newstr[2:findPos]
newstr2=newstr[0:2] + newstr[findPos+3:]

print(f"Original {str1} - new {newstr1}")   
print(f"Original {str2} - new {newstr2}")   