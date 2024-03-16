def pattern_match(pattern, s):
    pattern_dict = {}
    string_dict = {}

    for i, char in enumerate(pattern):
        if char not in pattern_dict:
            pattern_dict[char] = i

    for i, char in enumerate(s):
        if char not in string_dict:
            string_dict[char] = i

    return pattern_dict == string_dict


pattern = "abba"
s = "redblueredblue"

if pattern_match(pattern, s):
    print(True)
else:
    print(False)
    