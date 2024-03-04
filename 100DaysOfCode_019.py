def add_digits(num):
    # Convert the integer to a string for easier digit access.
    num_str = str(num)

    # While the string has more than one digit, repeatedly add its digits and update the string.
    while len(num_str) > 1:
        digit_sum = 0
        for digit in num_str:
            digit_sum += int(digit)
            num_str = str(digit_sum)
    # Return the single-digit result as an integer.
    return int(num_str)


# Example usage
num = 1996
all_single_sum = add_digits(num)
print(f"The single-digit sum of {num} is: {all_single_sum}")
