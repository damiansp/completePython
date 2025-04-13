from collections import Counter


words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',  'the',
    'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes',
    "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes',
    "you're", 'under']
word_counts = Counter(words)
top_3 = word_counts.most_common(3)
print(top_3)

more_words = ['why', 'are', 'you', 'not', 'looking', 'into', 'my', 'eyes']
#for word in more_words:
#    word_counts[word] += 1
word_counts.update(more_words)


# Combine counters
a = Counter(words)
b = Counter(more_words)
c = a + b
print(c)

d = a - b
print(d)
