# Can one block of except statements handle multiple exception?
#Yes try-except blocks can be used to catch and respond to one or multiple exceptions
#You can handle diff exception all using a singal block of code  and they can be grouped togeather 
# as a tuple.someetimes process can raise more than one possible exception , then they all
#can be handled using singal exception

try:
    name='Test'
    name+=5
except (NameError,TypeError) as e:
    print(e)


