def reverse_binary(data):
    binary = f'{data:08b}'
    print(data," ",binary)
    return int(binary[::-1], 2)

print(reverse_binary(2024))
