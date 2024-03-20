def hamming_distance(x, y):
    xor = x ^ y
    distance = 0
    while xor:
        distance += xor & 1
        xor >>= 1
    return distance


print(hamming_distance(1, 4))
print(hamming_distance(3, 1))
