# -*- coding: utf-8 -*-
#Importerer matplotlib.
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
#setter x og y verdier. Velger fargen på grafene.
plt.plot([0,0.2,0.4,0.6,0.8], [0, 0.00692, 0.0051, 0.6650, 0.652], 'r') #slow
plt.plot([0,0.2,0.4,0.6,0.8], [0, 0.00692, 0.0039, 0.0226, 0.0262], 'b') #fast

#bestemmer x og y aksene.
plt.axis([0, 1, 0, 1])

#tittelen å aksen.
ax.set_title("")
#Side tittelen på y aksen.
ax.set_ylabel('Tid i sekunder * 100')

plt.show()


"""
Referanse: Kodeen er hentet fra matplotlib.
http://matplotlib.org/users/pyplot_tutorial.html
"""
