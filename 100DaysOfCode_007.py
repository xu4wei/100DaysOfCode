# Enter three names and three ages, then enter the name to query their age
name_age = {}
for i in range(3):
    name = input("Name? ")
    age = int(input("Age? "))
    name_age[name] = age
name_select = input("Which Name to find? ")
if name_select in name_age:
    print(name_age[name_select])
else:
    print("The name you entered is not among the first three")