# Transfer the split words to a list
moby_words = []
with open('moby_01_clean.txt') as infile:
    for word in infile:
        if word.strip():
            moby_words.append(word.strip())
# Count the number of occurrences of each word and store it in the dictionary
word_count = {}
for word in moby_words:
    count = word_count.setdefault(word, 0)
    count += 1
    word_count[word] += 1
# Convert from dictionary format to list format
word_list = list(word_count.items())
# sort
word_list.sort(key=lambda x: x[1])
# Take the three with the most frequency
print("More times words:")
for word in reversed(word_list[-3:]):
    print(word)
# Take the three with the smallest number of times
print("\nLess times words:")
for word in word_list[:3]:
    print(word)