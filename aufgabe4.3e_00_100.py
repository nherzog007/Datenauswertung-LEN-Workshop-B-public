import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('4.3.e_00_100.csv', skiprows=2, dtype=float, delimiter=',')
freq = data[:, 0]
mag = data[:, 1]
phase_deg = data[:, 2]

fig, ax1 = plt.subplots(layout='constrained')
ax2 = ax1.twinx()
ax1.set_title('Aufgabe 4-3e ($R_1 = 0 \t{kΩ}, R_2 = 100 \t{kΩ}$)')
ax1.set_xscale('log')
ax1.plot(freq, mag, color='r', label='Magnitude')
ax2.plot(freq, phase_deg, color='b', label='Phase')
ax1.set_xlabel('Frequenz [Hz]')
ax1.set_ylabel('Magnitude [dB]', color='r')
ax2.set_ylabel('Phase [°]', color='b')
ax1.grid(True)
ax2.grid(True)
ax1.set_xlim(10**2, 10**4)
ax2.set_xlim(10**2, 10**4)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()