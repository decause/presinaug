import nltk
from nltk import FreqDist
from nltk.corpus import gutenberg
import json
import csv
import datetime


print "* Loading corpus"
# raw = gutenberg.raw('melville-moby_dick.txt')
# raw = gutenberg.raw('bible-kjv.txt')
# raw = gutenberg.raw('blake-poems.txt')

# Open a csv, read the whole thing
with open('presinaug-addresses.txt', "r") as f:
    raw = f.read()

print "* Tokenizing"
tokens = nltk.word_tokenize(raw)

print "* Tagging parts of speech"
# Save this to strip articles later
parts_of_speech = nltk.pos_tag(tokens)

print "* Converting POS list into a dict for lookup"
# TODO -- fix this.  this is going to have a hard time with homonyms
parts_of_speech = dict(parts_of_speech)

# You can ban other parts of speech by adding their tags to this list.
# You can find out what the part-of-speech tags mean by using code like
# this:
# >>> print nltk.help.upenn_tagset('DT')
# DT: determiner
#     all an another any both del each either every half la many much nary
#     neither no some such that the them these this those
banned_parts_of_speech = [
    'DT',
    'IN',
    'CC',
    'TO',
    'PRP',
    'PRP$',
]

banned_words = [
    'is',
    'In',
    'It',
    'to',
    'TO',
    'Too',
    'too',
    'Much',
    'much',
    'very',
    'are',
    'has',
    'had',
    'have',
    'there',
    'they',
    'this',
    'also',
    'Sir',
    'sir',
    'been',
    'so',
    'So',
    'on',
    'On',
    'did',
    'am',
    'are'
    'Is',
    'be',
    'my',
    'My',
    'can',
    'Can',
    'was',
    'of',
    'Of',
    'OF',
    'OH',
    'oh',
    'Oh',
    'the',
    'THE',
    'The',
    'Thee',
    'Thou',
    'that',
    'That',
    'Thy',
    'when',
    'When',
    'what',
    'What',
    'who',
    'Who',
    'how',
    'How',
    'his',
    'His',
    'were',
    'Why',
    'why',
    'then',
    'Then',
    'Does',
    'does',
    'O',
    'do',
    'Do',
    'Go',
    'go',
    'go',
    'As',
    'whom',
    'Whom',
]

print "* Stripping stuff we don't want"
# Strip punctuation and banned parts of speech
tokens = [
    token for token in tokens if (
        # remove punctuation
        token.isalpha() and
        # remove parts of speech that we don't want.
        not parts_of_speech[token] in banned_parts_of_speech and
        not token in banned_words #and
        #len(token) > 4
    )
]

print "* Building frequency distribution"
words = FreqDist(tokens)

n = 20

def showWords(n=10000):
    '''
    Open a CSV, write top n words to it, print top n words
    '''
    print "* Printing top %i words" % n
    f = open('presinaug.csv', 'wb')
    writer = csv.writer(f)
    for i, pair in enumerate(words.items()):
        word, count = pair
        row = word, count, parts_of_speech[word]
        # row = "%r, %r, %r" % (word, count, parts_of_speech[word])
        # row = json.dumps([word, count, parts_of_speech[word]], separators=(',',':'))
        writer.writerow(row)
        print "%r appeared %i times. Its part of speech is %r" % (
            word, count, parts_of_speech[word],
        )
        if i > n:
            break
    f.close()
    return (word, count, parts_of_speech)

showWords()
