def reverseWords(s):
    words = s.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return ' '.join(reversed_words)


s1 = "Let's take LeetCode contest"
s2 = "Mr Ding"
print(reverseWords(s1))
print(reverseWords(s2))
