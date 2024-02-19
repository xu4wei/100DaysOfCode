# Use the format() method to format strings
print("{1:{0}}".format(3,4))
print("{0:$>5}".format(3))
print("{a:{b}}".format(a=1,b=5))
print("{1:{b}}:{c:$>5}".format(3,4,a=1,b=5,c=10))