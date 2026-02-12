import string

file = open(file="sample-file.txt", mode="r") # open file
content = file.read()
tokens = content.split()
cleaned_tokens = []
for token in tokens:
    while len(token) > 0 and token[0]  in string.punctuation:
        token = token[1:]
    while len(token) > 0 and token[-1]  in string.punctuation:
        token = token[:-1]
    token = token.lower()
    cleaned_tokens.append(token)
print("After cleaning and converting to lowercase, the tokens would be:", cleaned_tokens)
words = {}
for token in cleaned_tokens:
    count = 0
    for char in token:
        if char.isalpha():
            count +=1
    if count >= 2:
        if token in words:
            words[token] += 1
        else:
            words[token] = 1
sorted_frequencies = sorted(words.items(),key=lambda word: word[1], reverse=True)

print("The word frequencies would be:")
for word, frequency in sorted_frequencies[:10]:
    print(f"{word} -> {frequency}")

file.close() #close file