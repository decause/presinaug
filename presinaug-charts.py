import pygal
import csv
from collections import defaultdict


partsofspeech = defaultdict(int)

#Slick csv-to-dict method. Shoutout @Qalthos
pos_legend = {}
with open('partsofspeech.csv', 'rb') as f:
    reader = csv.reader(f, delimiter="|")
    pos_legend = dict(reader)
    #print(pos_legend)


with open('presinaug.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        partsofspeech[row[2]] += int(row[1])
        #print(row)


xy_chart = pygal.XY(stroke=False)
xy_chart.title = 'Word Frequency of US Presidential Inaugural Addresses'

bar_chart = pygal.Bar(show_legend=False)
bar_chart.x_labels = sorted(partsofspeech.keys(), key=lambda x: partsofspeech[x], reverse=True)
bar_chart.x_label_rotation = 90
bar_chart.title = 'Parts of Speech in US Presidential Inaugural Addresses'

with open('presinaug.csv', 'rb') as f:
    reader = csv.reader(f)
    for rownum,row in enumerate(reader):
        # {row[0]}.format(row=row) is Just the label for the key, made by string formating 0th item in the row
        # [(rownum, int(row[1]))]) is a list of tuples, starting with the rownumber (from enum) and the 1st item in row
        xy_chart.add(row[0], [(rownum, int(row[1]))])

#for part,count in partsofspeech.items():
#    bar_chart.add("Count", count)
bar_chart.add("Count", sorted(partsofspeech.values(), reverse=True))

#xy_chart.render_in_browser()
#xy_chart.render_to_png('presinaug-words.png')
xy_chart.render_to_file('presinaug-words.svg')
bar_chart.render_to_file('presinaug-pos.svg')
