#coding: cp950
temperatures = []
with open('lab_05.txt') as infile:
    for row in infile:
        temperatures.append(float(row.strip()))

max_temp = max(temperatures)
min_temp = min(temperatures)
mean_temp = sum(temperatures)/len(temperatures)

# 逼 い计
temperatures.sort()
median_temp = temperatures[len(temperatures)//2]

print("程蔼放 = {}".format(max_temp))
print("程放 = {}".format(min_temp))
print("キА = {}".format(mean_temp))
print("い计 = {}".format(median_temp))

x = set(temperatures)
print("There are ",len(x)," different values")
