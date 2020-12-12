import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np

import locale
locale.setlocale(locale.LC_NUMERIC, "pt_BR")
plt.rcParams['axes.formatter.use_locale'] = True

df = pd.read_csv("./data/input/data.csv")

# ========
# Sensor 1
# ========
x_1 = df['temperatura']
y_1 = df['1'] * 1000
plt.figure(figsize=(7,5), dpi=300)
plt.scatter(x_1, y_1, s=8)

#curva de tendencia
z_1 = np.polyfit(x_1, y_1, 4)
p_1 = np.poly1d(z_1)
plt.plot(x_1, p_1(x_1), 'r--', label='Curva de tendência')

plt.axes().xaxis.set_minor_locator(tck.AutoMinorLocator())
plt.axes().yaxis.set_minor_locator(tck.AutoMinorLocator())
plt.grid(True, which='major', axis='both')

plt.title('Sensor 1')
plt.xlabel('T (°C)')
plt.ylabel('R (Ω)')
plt.legend()

plt.savefig('./data/output/sensor1.jpg')