def zeroes_to_end(data):
    for _ in range(data.count(0)):
        ind = data.index(0)
        data = data[:ind] + data[ind+1:] + data[ind:ind+1]
    return data


print(zeroes_to_end([2, 0, 2, 4, 0, 3, 0, 8]))
