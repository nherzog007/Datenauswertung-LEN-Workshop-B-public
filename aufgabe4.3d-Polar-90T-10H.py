import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('Aufgabe 4-d-90T-10H.txt', skiprows=1, dtype=str, encoding='latin1')
freq = data[:, 0].astype(float)

def ZahlenPruefung(val: str) -> float:
	allowed = '+-eE.'
	cleaned = ''.join(ch for ch in val if ch.isdigit() or ch in allowed)
	return float(cleaned)

raw = np.array([s.split(',') for s in data[:, 1]])
mag = np.array([ZahlenPruefung(x) for x in raw[:, 0]])
phase_deg_raw = np.array([ZahlenPruefung(x) for x in raw[:, 1]])
phase_deg = np.unwrap(np.deg2rad(phase_deg_raw)) * 180 / np.pi

fig, ax1 = plt.subplots(layout='constrained')
ax2 = ax1.twinx()
ax1.set_title('Aufgabe 4-d (Tiefpass: $90\Omega$, Hochpass: $10\Omega$)')
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