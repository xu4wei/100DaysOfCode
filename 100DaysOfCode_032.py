def reverseString(s):
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s


s = ["p", "y", "t", "h", "o", "n"]
reverseString(s)
print(s)
