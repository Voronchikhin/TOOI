import xml.etree.ElementTree as ET
import collections


def bigrams(wordsS):
    return zip(wordsS, wordsS[1:])


counter = collections.Counter()
tokens = list()
words = list()
tree = ET.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

for child in root.findall('text'):
    paragraphs = child.find('paragraphs')
    for paragraph in paragraphs:
        sentences = paragraph.findall('sentence')
        for sentence in sentences:
            for word in sentence.find('source').text.split(" "):
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
