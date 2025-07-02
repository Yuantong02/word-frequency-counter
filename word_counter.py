# word_counter.py

# Open the text file
f = open('sample.txt', 'r')
text = f.read()
f.close()

# Convert all text to lowercase and split into words
words = text.lower().split()

# Create an empty dictionary to store word frequencies
freq = {}

# Count the frequency of each word
for word in words:
    # Remove punctuation from each word
    word = word.strip('.,!?";:')
    if word:
        freq[word] = freq.get(word, 0) + 1

# Sort the dictionary by frequency in descending order
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# Print the top 10 most frequent words
for word, count in sorted_freq[:10]:
    print(word, count)