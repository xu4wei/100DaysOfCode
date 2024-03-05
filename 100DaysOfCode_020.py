def find_words(words):
    # Define the three rows of the keyboard.
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")

    # Initialize an empty list to store the valid words.
    valid_words = []

    # Loop through each word in the list.
    for word in words:
        word = word.lower()

    # Check if all letters of the word belong to the same row.
        if set(word) <= row1 or set(word) <= row2 or set(word) <= row3:
            valid_words.append(word)

    # Return the list of valid words.
    return valid_words


words = ["hall", "Python", "Windows", "upper"]
print(find_words(words))
