def reverseWords(s):
    # Split the string into words.
    words = s.split()
    # Reverse the order of the words.
    words.reverse()
    # Join the words back into a string with a single space separator.
    return " ".join(words)


s1 = "the sky is blue"
s2 = "  hello world  "
s3 = "a good   example"
print(reverseWords(s1))
print(reverseWords(s2))
print(reverseWords(s3))
