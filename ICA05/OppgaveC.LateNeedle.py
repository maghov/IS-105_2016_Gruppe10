# -*- coding: utf-8 -*-
#Importerer matplotlib.
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
#bestemmer x og y verdier. Velger fargen på grafene.
plt.plot([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9], [0, 0.0055, 0.0072, 0.0081, 0.099, 0.137, 0.145, 0.176, 0.193, 0.212], 'r') #slow
plt.plot([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9], [0, 0.0055, 0.0074, 0.0089, 0.092, 0.126, 0.145, 0.170, 0.190, 0.210 ], 'b') #fast

#bestemmer x og y aksene.
plt.axis([0, 0.9, 0, 0.7])

#tittelen å aksen.
ax.set_title("")
#Side tittelen på y aksen.
ax.set_ylabel('Tid i sekunder * 100')

plt.show()


"""
Kilde: Kodeen er hentet fra matplotlib.
http://matplotlib.org/users/pyplot_tutorial.html
"""
