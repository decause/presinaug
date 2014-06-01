presinaug
=====
This repository contains a suite of scripts used for Grokking Presidentinal
Inaugural Addresses from George Washington to Barack Obama.

*Fun with NLTK, pygal, and word_cloud*

[NLTK](http://nltk.org "NLTK")
---
Analyze the full-text, tag parts of speech, provide word frequency
distirbutions

[pygal](http://pygal.org "pygal")
---
Create a barchart showing the Parts of Speech in the form of an .svg

[word_cloud](https://github.com/amueller/word_cloud "word_cloud")
---
Generate a wordcloud (independent from NLTK) in the form of a .png

![alt text](https://raw.github.com/decause/presinaug/master/presinaug-wordcloud-1600x900.png "Presinaug WordCloud - Washington to Obama")
![alt text](https://raw.github.com/decause/presinaug/master/presinaug-pos.png "Presinaug Parts of Speech - Washington to Obama")
  

How it was done:
---
- wget the full set of texts
- strip of the gutenberg specific language (but keep the original file for
  attribution's sake)
- run the presinaug-nltk.py
- run the presinaug-charts.py
- run the presinaug-cloud.py


Installing
---

Though these are disparate tools, you can install each to run the component
scripts manually. Start with:


`pip install Cython`

This above line goes into an `install_requires` section in a proper setup.py (coming soon).

After that, you then run:

`pip install -r requirements.txt`

which should contain all the component libraries you'll need


Authors
---

 - Ralph Bean <rbean@redhat.com>
 - Nate Case <qalthos@gmail.com>
 - Remy DeCausemaker <remyd@civx.us>
