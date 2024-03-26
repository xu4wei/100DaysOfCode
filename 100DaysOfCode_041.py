def reverseStr(s, k):
    result = []
    for i in range(0, len(s), 2 * k):
        # Reverse the first k characters of the current 2k block.
        result.append(s[i:i + k][::-1])
        # Append the remaining characters of the current 2k block.
        result.append(s[i + k:i + 2 * k])
    return ''.join(result)


s1 = "abcdefg"
s2 = "abcd"
print(reverseStr(s1, 2))
print(reverseStr(s2, 2))
