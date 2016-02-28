import numpy as np
import matplotlib.pyplot as plt

N = 3
slow_tid = (0.00692105293274, 0.00519990921021, 0.0650689601898)
#slow_slow = (0, 0, 0, 0)

ind = np.arange(N)  # the x locations for the groups
width = 0.25       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, slow_tid, width, color='r')

fast_tid = (0.00692105293274, 0.00393009185791, 0.0226318836212)
#fast_fast = (3, 5, 2, 3)
rects2 = ax.bar(ind + width, fast_tid, width, color='b')

# add some text for labels, title and axes ticks
ax.set_ylabel('Tid i MS - TimeIt = 10')
ax.set_title('Slow og Fast algorittmer')
ax.set_xticks(ind + width)
ax.set_xticklabels(('Haystack = 1k \n Needle = 100', 'Haystack = 10k \n Needle = 1k', 'Haystack = 100k \n Needle = 10k'))

ax.legend((rects1[0], rects2[0]), ('Slow', 'Fast' 'h=haystack'))


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
