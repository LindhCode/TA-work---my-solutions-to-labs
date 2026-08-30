def tokenize(content):
    tokens = []
    current_word = ""

    for line in content:
        for letter in line:
            if letter.isalnum():
                if current_word and current_word[-1].isdigit() != letter.isdigit():
                    tokens.append(current_word)
                    current_word = ""
                current_word += letter.lower()
            else: 
                if current_word:
                    tokens.append(current_word)
                    current_word = ""
                if not letter.isspace():
                    tokens.append(letter)
    if current_word:
        tokens.append(current_word)
    return tokens

def countWords(words, stopWords):
    freq = {}
    for i in words:
        if i not in stopWords:
            freq[i] = freq.get(i, 0) + 1
    return freq


def printTopMost(frequencies, n):
    sorted_freqs = sorted(frequencies, key=lambda x: frequencies[x], reverse=True)
    if len(frequencies) < n:
        count = len(frequencies)
    else:
        count = n

    if count > 0: 
        for i in range(count):
            print(sorted_freqs[i].ljust(20) + str(frequencies[sorted_freqs[i]]).rjust(5))
