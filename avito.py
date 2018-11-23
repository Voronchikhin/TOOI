import csv
import collections


def bigrams(wordsS):
    return zip(wordsS, wordsS[1:])


with open('../stage3_test.csv', newline='', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list

    counter = collections.Counter()
    words = list()
    for row in reader:
        rows.append(row)
        for word in row["Description"].split():
            if len(word) > 3:
                counter[word] += 1
                words.append(word)

        for word in row["Title"].split():
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
    bigramCounter.update(bigrams(words))
    # 20 most common bigrams
    print(bigramCounter.most_common(20))
    # sorted
    print(sorted(reader, key=lambda d: float(d['Price'])))
