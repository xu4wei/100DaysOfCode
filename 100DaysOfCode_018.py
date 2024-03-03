def length_of_last_word(s):
    # Strip any leading or trailing whitespace.
    s = s.strip()

    # If the string is empty, return 0.
    if not s:
        return 0

    # Split the string into words.
    words = s.split()

    # Return the length of the last word.
    return len(words[-1])


print("The last word with length:", end=" ")
print(length_of_last_word("Do not be like them"))
