#!/usr/bin/env python2

from os import path
import sys
import wordcloud

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'presinaug-addresses.txt')).read()
# Separate into a list of (word, frequency).
words = wordcloud.process_text(text, max_features=10000)
# Compute the position of the words.
elements = wordcloud.fit_words(words, width=900, height=1600)
# Draw the positioned words to a PNG file.
wordcloud.draw(elements, path.join(d, 'presinaug-wordcloud-1600x900.png'), width=900, height=1600,
        scale=1)
