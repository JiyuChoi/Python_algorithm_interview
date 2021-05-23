from collections import Counter
import re

def mostCommonWord(paragraph, banned):
    words = [word for word in re.sub('[^\w]', ' ', paragraph)
        .lower().split()
        if word not in banned]

    counts = Counter(words)
    return counts.most_common(1)[0][0]

# input
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(mostCommonWord(paragraph, banned))