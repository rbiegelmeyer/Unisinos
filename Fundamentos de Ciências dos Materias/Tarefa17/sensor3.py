import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np

import locale
locale.setlocale(locale.LC_NUMERIC, "pt_BR")
plt.rcParams['axes.formatter.use_locale'] = True

df = pd.read_csv("./data/input/data.csv")

# TEMPERATURA_AMBIENTE = 22.2
offset_tempopar = 0.879
df['3_1'] = df['3'] + offset_tempopar
df = df.round(3)

# ========
# Sensor 3
# ========
x_3 = df['temperatura']
y_3 = df['3_1']
plt.figure(figsize=(7,5), dpi=300)
plt.scatter(x_3, y_3, s=8)

#curva de tendencia
z_3 = np.polyfit(x_3, y_3, 2)
p_3 = np.poly1d(z_3)
plt.plot(x_3, p_3(x_3), 'r--', label='Curva de tendência')

plt.axes().xaxis.set_minor_locator(tck.AutoMinorLocator())
plt.axes().yaxis.set_minor_locator(tck.AutoMinorLocator())
plt.grid(True, which='major', axis='both')

plt.title('Sensor 3')
plt.xlabel('T (°C)')
plt.ylabel('V (mV)')
plt.ylim(bottom=0)
plt.legend()

plt.savefig('./data/output/sensor3.jpg')

df.to_csv(r'./save.csv')