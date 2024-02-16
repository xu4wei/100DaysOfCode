'''
Take the last 3 elements of a list with 10 elements
Move to the beginning and keep the original order
'''
x = [0,1,2,3,4,5,6,7,8,9]
x.extend(x[:7])
del x[:7]
print(x)