def ceaser(text):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) - 62) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) - 94) % 26 + 97)
    return result


text = "Hello Python World"

print("Original Text: " + text)
print("Caesar Cipher: " + ceaser(text))
