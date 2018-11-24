import csv
import collections
import json


def bigrams(wordsS):
    return zip(wordsS, wordsS[1:])


counter = collections.Counter()
tokens = list()
words = list()
with open('RomeoAndJuliet.json') as f:
    data = json.load(f)
    for acts in data['acts']:
        for scenes in acts['scenes']:
            for actions in scenes['action']:
                for phrase in actions['says']:
                    for word in phrase.split(" "):
                        tokens.append(word)
                        if len(word) > 3:
                            counter[word] += 1
                            words.append(word)

# 20 наиболее часто встречаемых
print(counter.most_common(20))
# 20 наименее часто встречаемых
print(counter.most_common()[:-20 - 1:-1])
# самое длинное слово
print(max(counter.elements(), key=len))
# total unique
print(len(counter))
# total words
print(len(list(counter.elements())))

bigramCounter = collections.Counter()
bigramCounter.update(bigrams(tokens))
# 20 most common bigrams
print(bigramCounter.most_common(20))
