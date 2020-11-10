import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from scipy import signal
import numpy as np

sys = signal.TransferFunction([7000], [1,7000])

w, mag, phase = signal.bode(sys)

# Plot Bode
plt.figure()
plt.semilogx(w, mag, color='black')                                       # Bode magnitude plot
plt.title('Frequency x Magnitude')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Magnitude (dB)')
plt.axvline(x=7000, color='black', linestyle=':')
plt.axhline(y=-3, color='black', linestyle=':')
plt.axes().yaxis.set_minor_locator(tck.AutoMinorLocator())
plt.grid(True, which='major', axis='y')
plt.grid(True, which='both', axis='x')
plt.savefig('imagens/freqXmag_2.png')

plt.figure()
plt.semilogx(w, phase, color='black')                                     # Bode phase plo
plt.title('Frequency x Phase')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Phase (deg)')
plt.axvline(x=7000, color='black', linestyle=':')
plt.axhline(y=-45, color='black', linestyle=':')
plt.axes().yaxis.set_minor_locator(tck.AutoMinorLocator())
plt.grid(True, which='major', axis='y')
plt.grid(True, which='both', axis='x')
plt.savefig('imagens/freqXpha_2.png')


# plt.show()