#Why do you use Zip() Method in python?
#Zip method is used for paired first item in each passed iterator togeather and then second item in each passed iterator paired togeatger
#zip returns zip object so u have to convert it either list,tuple,set,dictionary
#if two iterator have diff lengths then iterator of least item decides the length of new iterator 

d1=("V","VI","VII")
d2=(50,80)

d3=zip(d1,d2)
print(list(d3))
