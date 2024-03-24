def detectCapitalUse(word):
    # Check if all letters are capitals
    if word.isupper():
        return True

    # Check if all letters are not capitals
    if word.islower():
        return True

    # Check if only the first letter is capital
    if word[0].isupper() and word[1:].islower():
        return True

    # Otherwise, the usage of capitals is wrong
    return False


word1 = "USA"
word2 = "FlaG"
word3 = "leetcode"
word4 = "Google"
print(detectCapitalUse(word1))
print(detectCapitalUse(word2))
print(detectCapitalUse(word3))
print(detectCapitalUse(word4))
