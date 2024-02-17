#coding: cp950
temperatures = []
with open('lab_05.txt') as infile:
    for row in infile:
        temperatures.append(float(row.strip()))

max_temp = max(temperatures)
min_temp = min(temperatures)
mean_temp = sum(temperatures)/len(temperatures)

# 排序 中位數
temperatures.sort()
median_temp = temperatures[len(temperatures)//2]

print("最高溫度 = {}".format(max_temp))
print("最低溫度 = {}".format(min_temp))
print("平均值 = {}".format(mean_temp))
print("中位數 = {}".format(median_temp))

x = set(temperatures)
print("There are ",len(x)," different values")
