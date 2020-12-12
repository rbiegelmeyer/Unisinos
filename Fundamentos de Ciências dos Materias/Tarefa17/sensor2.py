import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np

import locale
locale.setlocale(locale.LC_NUMERIC, "pt_BR")
plt.rcParams['axes.formatter.use_locale'] = True

df = pd.read_csv("./data/input/data.csv")
df.round(3)

# ========
# Sensor 2
# ========
x_2 = df['temperatura']
y_2 = df['2'] * 1000
plt.figure(figsize=(7,5), dpi=300)
plt.scatter(x_2, y_2, s=8)

#curva de tendencia
z_2 = np.polyfit(x_2, y_2, 2)
p_2 = np.poly1d(z_2)
plt.plot(x_2, p_2(x_2), 'r--', label='Curva de tendência')

plt.axes().xaxis.set_minor_locator(tck.AutoMinorLocator())
plt.axes().yaxis.set_minor_locator(tck.AutoMinorLocator())
plt.grid(True, which='major', axis='both')

plt.title('Sensor 2')
plt.xlabel('T (°C)')
plt.ylabel('R (Ω)')
plt.legend()

plt.savefig('./data/output/sensor2.jpg')
