#coding: cp950
temperatures = []
with open('lab_05.txt') as infile:
    for row in infile:
        temperatures.append(float(row.strip()))

max_temp = max(temperatures)
min_temp = min(temperatures)
mean_temp = sum(temperatures)/len(temperatures)

# �Ƨ� �����
temperatures.sort()
median_temp = temperatures[len(temperatures)//2]

print("�̰��ū� = {}".format(max_temp))
print("�̧C�ū� = {}".format(min_temp))
print("������ = {}".format(mean_temp))
print("����� = {}".format(median_temp))

x = set(temperatures)
print("There are ",len(x)," different values")
