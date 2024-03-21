def find_complement(n):
    # Find the binary representation of the number.
    binary_string = bin(n)[2:]

    # Invert all the bits in the binary representation.
    inverted_binary_string = ''.join(['1' if bit == '0' else '0' for bit in binary_string])

    # Convert the inverted binary string back to an integer.
    complement = int(inverted_binary_string, 2)

    return complement


print(find_complement(5))
print(find_complement(1))
