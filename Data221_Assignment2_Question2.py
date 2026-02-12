import string
#open file
file = open(file="sample-file.txt", mode="r")
#read file
content = file.read()
#split into tokens
tokens = content.split()
cleaned_tokens = []

#clean and lowercase tokens
for token in tokens:
    while len(token) > 0 and token[0]  in string.punctuation:
        token = token[1:]
    while len(token) > 0 and token[-1]  in string.punctuation:
        token = token[:-1]
    token = token.lower()
    cleaned_tokens.append(token)
print("After cleaning and converting to lowercase, the tokens would be:", cleaned_tokens)
tokens_with_2_or_more_alphabetics= {}
for token in cleaned_tokens:
    count = 0
    for char in token:
        if char.isalpha():
            count +=1
    if count >= 2:
        if token in tokens_with_2_or_more_alphabetics:
            tokens_with_2_or_more_alphabetics[token] += 1
        else:
            tokens_with_2_or_more_alphabetics[token] = 1
sorted_frequencies = sorted(tokens_with_2_or_more_alphabetics.items(),key=lambda word: word[1], reverse=True)

print("The word frequencies would be:")
for word, frequency in sorted_frequencies[:10]:
    print(f"{word} -> {frequency}")

#contruct bigrams
bigrams = []
for i in range(len(cleaned_tokens)-1):
    bigram = cleaned_tokens[i] + " " + cleaned_tokens[i+1]
    bigrams.append(bigram)

# count bigram
bigram_counts= {}

for bigram in bigrams:
    if bigram in bigram_counts:
        bigram_counts[bigram] += 1
    else:
        bigram_counts[bigram] = 1
sorted_bigrams_frequencies = sorted(bigram_counts.items(), key=lambda bigram: bigram[1], reverse=True)

print("The bigram frequencies would include:")

for bigram, frequency in sorted_bigrams_frequencies[:5]:
    print(f"{bigram} -> {frequency}")
file.close()