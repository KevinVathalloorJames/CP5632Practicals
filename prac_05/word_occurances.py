words_for_count = {}
text = input("Text: ")

words_splitted = text.split()

for words in words_splitted:
    key = words_for_count.get(words, 0)
    words_for_count[words] = key+1

words = list(words_for_count.keys())
words.sort()

maximum_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, maximum_length, words_for_count[word]))
