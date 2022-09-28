#What happens when „1‟== 1 is executed
#it simply returns false does not generate any exception

try:
    a="1"==1
    print(a)
except Exception as e:
    print(e)