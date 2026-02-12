import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('4.3f_100_0.csv', skiprows=2, dtype=float, delimiter=',')
zeit = data[:, 0]
spannung = data[:, 1]

fig, ax1 = plt.subplots(layout='constrained')
ax1.set_title('Aufgabe 4-3f ($R_1 = 100 \t{kΩ}, R_2 = 0 \t{kΩ}$)')
ax1.plot(zeit, spannung, color='r', label='Spannung')
ax1.set_xlabel('Zeit [s]')
ax1.set_ylabel('Spannung [V]', color='r')
ax1.grid(True)
ax1.set_xlim(-6, 6)
ax1.legend(loc='upper left')

plt.show()