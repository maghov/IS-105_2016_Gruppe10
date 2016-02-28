import numpy as np
import matplotlib.pyplot as plt

N = 4
slow_tid = (21, 35, 30, 35)
slow_slow = (0, 0, 0, 0)

ind = np.arange(N)  # the x locations for the groups
width = 0.25       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, slow_tid, width, color='r',yerr=slow_tid)

fast_tid = (25, 32, 34, 20)
#fast_fast = (3, 5, 2, 3)
rects2 = ax.bar(ind + width, fast_tid, width, color='b')

# add some text for labels, title and axes ticks
ax.set_ylabel('Tid')
ax.set_title('Slow og Fast algorittmer')
ax.set_xticks(ind + width)
ax.set_xticklabels(('Haystack = 1k \n Needle = 100', 'Haystack = 10k \n Needle = 1k', 'Haystack = 100k \n Needle = 10k', "Haystack = 1 Mill \n Needle = 100k"))

ax.legend((rects1[0], rects2[0]), ('Slow', 'Fast'))


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
