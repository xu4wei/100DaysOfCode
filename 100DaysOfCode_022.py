def find_miss_nums(data):
    all_data = set(range(1, len(data) + 1))
    return list(all_data - set(data))


nums = [1, 3, 4, 6, 4, 0]
print(find_miss_nums(nums))
