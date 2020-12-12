import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np

import locale
locale.setlocale(locale.LC_NUMERIC, "pt_BR")
plt.rcParams['axes.formatter.use_locale'] = True

df = pd.read_csv("./data.csv")
x_1 = df['F']


plt.figure(figsize=(7,5), dpi=300)


# ==============
# Extensometro 1
# V = 1V
# ==============
label = 'Extensômetro 1 (V = 1V)'
color = 'blue'
y_1 = df['1']
z_1 = np.polyfit(x_1, y_1, 1)
p_1 = np.poly1d(z_1)
t_1 = p_1(x_1)

plt.scatter(x_1, y_1, s=8, color=color)
plt.plot(x_1, t_1,color=color, linestyle='dashed', label=label)


# ==============
# Extensometro 1
# V = 2V
# ==============
label = 'Extensômetro 1 (V = 2V)'
color = 'red'
y_1 = df['2']
z_1 = np.polyfit(x_1, y_1, 1)
p_1 = np.poly1d(z_1)
t_1 = p_1(x_1)

plt.scatter(x_1, y_1, s=8, color=color)
plt.plot(x_1, t_1,color=color, linestyle='dashed', label=label)

# ==============
# Extensometro 1
# V = 3V
# ==============
label = 'Extensômetro 1 (V = 3V)'
color = 'orange'
y_1 = df['3']
z_1 = np.polyfit(x_1, y_1, 1)
p_1 = np.poly1d(z_1)
t_1 = p_1(x_1)

plt.scatter(x_1, y_1, s=8, color=color)
plt.plot(x_1, t_1,color=color, linestyle='dashed', label=label)

# ==============
# Extensometro 2
# V = 1V
# ==============
label = 'Extensômetro 2 (V = 1V)'
color = 'purple'
y_1 = df['4']
z_1 = np.polyfit(x_1, y_1, 1)
p_1 = np.poly1d(z_1)
t_1 = p_1(x_1)

plt.scatter(x_1, y_1, s=8, color=color)
plt.plot(x_1, t_1,color=color, linestyle='dashed', label=label)

# ==============
# Extensometro 2
# V = 2V
# ==============
label = 'Extensômetro 2 (V = 2V)'
color = 'green'
y_1 = df['5']
z_1 = np.polyfit(x_1, y_1, 1)
p_1 = np.poly1d(z_1)
t_1 = p_1(x_1)

plt.scatter(x_1, y_1, s=8, color=color)
plt.plot(x_1, t_1,color=color, linestyle='dashed', label=label)

# ==============
# Extensometro 2
# V = 3V
# ==============
label = 'Extensômetro 2 (V = 3V)'
color = 'black'
y_1 = df['6']
z_1 = np.polyfit(x_1, y_1, 1)
p_1 = np.poly1d(z_1)
t_1 = p_1(x_1)

plt.scatter(x_1, y_1, s=8, color=color)
plt.plot(x_1, t_1,color=color, linestyle='dashed', label=label)




plt.axes().xaxis.set_minor_locator(tck.AutoMinorLocator())
plt.axes().yaxis.set_minor_locator(tck.AutoMinorLocator())
plt.grid(True, which='major', axis='both')

# plt.title('Sensor 1')
plt.xlabel('Força (N)')
plt.ylabel('Tensão (mV)')
plt.legend()

plt.savefig('./sensor1.jpg')