def find_majority_num(data):
    counter = [(data.count(i), i) for i in set(data)]
    print("(Frequency,Element): ", counter)
    return sorted(counter, reverse=True)[0][1]


print(find_majority_num([2, 3, 3, 4, 4, 4, 4, 5, 7, 6]))
