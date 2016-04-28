# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

N = 4 # antall grafer
slow_tid_needle100k = (65.28, 71.89, 43.54, 44.62)


ind = np.arange(N)
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(ind, slow_tid_needle100k, width, color='r')

slow_tid_needle900k = (60.88, 71.31, 41.27, 43.98)

rects2 = ax.bar(ind + width, slow_tid_needle900k, width, color='b')

ax.set_ylabel('Tid i sekunder * 100')
ax.set_title('Search_Slow Algoritme - Haystack = 1 million')
ax.set_xticks(ind + width)
ax.set_xticklabels(('Magnus', 'Erik', 'Mohammad/John/Eirik', 'Per'))

ax.legend((rects1[0], rects2[0]), ('Needle=100k', 'Needle=900k'))


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()

"""
Referanse:
http://matplotlib.org/examples/api/barchart_demo.html
"""
