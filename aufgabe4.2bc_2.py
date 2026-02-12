import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('4.2bc_osci2.csv', skiprows=2, dtype=float, delimiter=',')
zeit = data[:, 0]
spannung_Hochpass = data[:, 1]
spannung_Tiefpass = data[:, 2]

fig, ax1 = plt.subplots(layout='constrained')
ax1.set_title('Aufgabe 4-2bc Oszilloskop $10$kHz')
ax1.plot(zeit, spannung_Hochpass, color='r', label='U Hochpass')
ax1.plot(zeit, spannung_Tiefpass, color='b', label='U Tiefpass')
ax1.set_xlabel('Zeit [ms]')
ax1.set_ylabel('Spannung [V]')
ax1.grid(True)
ax1.set_xlim(-3, 3)
ax1.legend(loc='upper left')

plt.show()