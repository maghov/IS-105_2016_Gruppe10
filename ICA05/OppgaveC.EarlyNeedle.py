# -*- coding: utf-8 -*-
#Importerer matplotlib.
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
#setter x og y verdier. Velger fargen på grafene.
plt.plot([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9], [0, 0.00065, 0.0072, 0.0051, 0.079, 0.097, 0.1, 0.1034, 0.3045, 0.7650], 'r') #slow
plt.plot([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9], [0, 0.0006, 0.00692, 0.0039, 0.022, 0.0262, 0.034, 0.099, 0.1, 0.156 ], 'b') #fast

#bestemmer x og y aksene.
plt.axis([0, 0.9, 0, 0.7])

#tittelen å aksen.
ax.set_title("")
#Side tittelen på y aksen.
ax.set_ylabel('Tid i sekunder * 100')

plt.show()


"""
Referanse: Kodeen er hentet fra matplotlib.
http://matplotlib.org/users/pyplot_tutorial.html
"""
