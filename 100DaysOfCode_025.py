def reverse_num(data):
    answer = int(str(abs(data))[::-1]) * (1 if data >= 0 else -1)
    return answer


print(reverse_num(-2024))
print(reverse_num(1234))
print(reverse_num(-310))
