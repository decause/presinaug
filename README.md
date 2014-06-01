presinaug
=====

Suite of scripts for Grokking Presidentinal Inaugural Addresses

Fun with NLTK, pygal, and word_cloud

NLTK
    - Analyze the full-text, tag parts of speech, provide word frequency
      distirbutions
pygal
    - Create a barchart showing the Parts of Speech in the form of an .svg

word_cloud
    - Generage a wordcloud (independent from NLTK) in the form of a .png

![alt text](https://raw.github.com/decause/presinaug/master/presinaug-wordcloud-1600x900.png "Presinaug WordCloud - Washington to Obama")
![alt text](https://raw.github.com/decause/presinaug/master/presinaug-pos.png "Presinaug Parts of Speech - Washington to Obama")
  

How it was done:
---
- wget the full set of texts
- strip of the gutenberg specific language (keep original for attribution
  though)
- run the presinaug-nltk.py
- run the presinaug-charts.py
- run the presinaug-cloud.py

Get the full set of texts
---
 - wget http://www.gutenberg.org/cache/epub/4938/pg4938.txt




