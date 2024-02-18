# Replace punctuation with spaces
pun = str.maketrans("!.,:;-?", "       ")
x = "This is text, with: punctuation! Right?"
x = x.translate(pun)
print(x)