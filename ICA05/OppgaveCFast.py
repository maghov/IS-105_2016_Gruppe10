import numpy as np
import matplotlib.pyplot as plt

N = 4 # antall grafer
fast_tid_needle100k = (26.25, 21.76, 19.04, 17.84)


ind = np.arange(N)  
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(ind, fast_tid_needle100k, width, color='r') 

fast_tid_needle900k = (58.54, 65.13, 38.61, 41.72)

rects2 = ax.bar(ind + width, fast_tid_needle900k, width, color='b')

ax.set_ylabel('Tid i sekunder * 100')
ax.set_title('Search_Fast Algoritme - Haystack = 1 million')
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