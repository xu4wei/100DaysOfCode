class Solution:
    def reverseVowels(self, s):
        chars = list(s)
        vowel = ['a', 'e', 'i', 'o', 'u']
        index = []
        vowels = []
        for i in range(len(chars)):
            if chars[i] in vowel:
                vowels.append(chars[i])
                index.append(i)
        vowels = vowels[::-1]
        final = []
        ind = 0
        for i in range(len(chars)):
            if i in index:
                final.append(vowels[ind])
                ind += 1
            else:
                final.append(chars[i])
        str1 = ""
        return str1.join(final)


s = Solution()
print(s.reverseVowels("hello"))
print(s.reverseVowels("leetcode"))
