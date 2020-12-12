import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from math import pi

import locale
locale.setlocale(locale.LC_NUMERIC, "pt_BR")
plt.rcParams['axes.formatter.use_locale'] = True

sae = {
    'ci': 40e-3,
    'di': 8e-3,
    'cf': 46.5e-3,
    'df': 5.6e-3
}
sae['A'] = pi*((sae['di']/2.0)**2)

al = {
    'ci': 40e-3,
    'di': 8e-3,
    'cf': 47.6e-3,
    'df': 5.6e-3
}
al['A'] = pi*((al['di']/2.0)**2)

latao = {
    'ci': 40e-3,
    'di': 8e-3,
    'cf': 48.42e-3,
    'df': 6.5e-3
}
latao['A'] = pi*((latao['di']/2.0)**2)


# =====================================================================
# =========================== SAE 1045 ================================
# =====================================================================
df_sae = pd.read_csv("./data/input/sae_1045.csv")
df_sae['tensao'] = (df_sae['load_kN'] * 1000) / sae['A'] / 1e6
df_sae['deformacao'] = (df_sae['Actuator_mm'] / 1000) / sae['ci']
# Linha Linear
df_sae['deformacao_linear'] = df_sae['tensao'] * df_sae['deformacao'].iloc[10]/df_sae['tensao'].iloc[10]

sae_limite_proporcionalidade = 350
sae_tensao_escoamento = 747
sae_tensao_max = 822 #df_sae['tensao'].max()
sae_tensao_ruptura = 635
sae_def_lim = 0.18


# =====================================================================
# =========================== Aluminio ================================
# =====================================================================
df_al = pd.read_csv("./data/input/al.csv")
df_al['tensao'] = (df_al['load_kN'] * 1000) / al['A'] / 1e6
df_al['deformacao'] = (df_al['Actuator_mm'] / 1000) / al['ci']
df_al['deformacao_linear'] = df_al['tensao'] * df_al['deformacao'].iloc[10]/df_al['tensao'].iloc[10]

al_limite_proporcionalidade = 200
al_tensao_escoamento = 240
al_tensao_max = 330 #df_al['tensao'].max()
al_tensao_ruptura = 242
al_def_lim = 0.215

# =====================================================================
# ============================ Latao ==================================
# =====================================================================
df_latao = pd.read_csv("./data/input/latao.csv")
df_latao['tensao'] = (df_latao['load_kN'] * 1000) / latao['A'] / 1e6
df_latao['deformacao'] = (df_latao['Actuator_mm'] / 1000) / latao['ci']
df_latao['deformacao_linear'] = df_latao['tensao'] * df_latao['deformacao'].iloc[30]/df_latao['tensao'].iloc[30]

latao_limite_proporcionalidade = 180
latao_tensao_escoamento = 378
latao_tensao_max = 498
latao_tensao_ruptura = 465
latao_def_lim = 0.25

# =====================================================================
# =========================== SAE 1045 ================================
# =====================================================================
plt.figure(figsize=(15,10), dpi=400)
plt.title('SAE 1045', fontsize=30)
plt.ylabel('σ (MPa)', fontsize=25)
plt.xlabel('Ɛ', fontsize=25)
plt.plot(df_sae['deformacao'], df_sae['tensao'])
# Linha Linear
# plt.plot(df_sae['deformacao_linear'], df_sae['tensao'])

plt.hlines(sae_limite_proporcionalidade, 0, sae_def_lim, colors='purple', linestyles='--', label='Limite de Proporcionalidade')
plt.hlines(sae_tensao_escoamento, 0, sae_def_lim, colors='green', linestyles='--', label='Tensão de Escoamento')
plt.hlines(sae_tensao_max, 0, sae_def_lim, colors='orange', linestyles='--', label='Tensão Máxima')
plt.hlines(sae_tensao_ruptura, 0, sae_def_lim, colors='red', linestyles='--', label='Tensão de Ruptura')

plt.axes().xaxis.set_minor_locator(tck.AutoMinorLocator())
plt.axes().yaxis.set_minor_locator(tck.AutoMinorLocator())
plt.grid(True, which='major', axis='both')
plt.legend(prop={'size': 20})
plt.savefig('./data/output/images/sae_1045.jpg')

# =====================================================================
# =========================== Aluminio ================================
# =====================================================================
plt.figure(figsize=(15,10), dpi=300)
plt.title('Alumínio', fontsize=30)
plt.ylabel('σ (MPa)', fontsize=25)
plt.xlabel('Ɛ', fontsize=25)
plt.plot(df_al['deformacao'],df_al['tensao'])
# plt.plot(df_al['deformacao_linear'], df_al['tensao'])
# plt.plot(df_al['deformacao_linear'] + df_al['deformacao'].max() * 0.002, df_al['tensao'])

plt.hlines(al_limite_proporcionalidade, 0, al_def_lim, colors='purple', linestyles='--', label='Limite de Proporcionalidade')
plt.hlines(al_tensao_escoamento, 0, al_def_lim, colors='green', linestyles='--', label='Tensão de Escoamento')
plt.hlines(al_tensao_max, 0, al_def_lim, colors='orange', linestyles='--', label='Tensão Máxima')
plt.hlines(al_tensao_ruptura, 0, al_def_lim, colors='red', linestyles='--', label='Tensão de Ruptura')


plt.axes().xaxis.set_minor_locator(tck.AutoMinorLocator())
plt.axes().yaxis.set_minor_locator(tck.AutoMinorLocator())
plt.grid(True, which='major', axis='both')
plt.legend(prop={'size': 20})
plt.savefig('./data/output/images/al.jpg')


# =====================================================================
# ============================ Latao ==================================
# =====================================================================
plt.figure(figsize=(15,10), dpi=300)
plt.title('Latão', fontsize=30)
plt.ylabel('σ (MPa)', fontsize=25)
plt.xlabel('Ɛ', fontsize=25)
plt.plot(df_latao['deformacao'],df_latao['tensao'])
# plt.plot(df_latao['deformacao_linear'], df_latao['tensao'])

plt.hlines(latao_limite_proporcionalidade, 0, latao_def_lim, colors='purple', linestyles='--', label='Limite de Proporcionalidade')
plt.hlines(latao_tensao_escoamento, 0, latao_def_lim, colors='green', linestyles='--', label='Tensão de Escoamento')
plt.hlines(latao_tensao_max, 0, latao_def_lim, colors='orange', linestyles='--', label='Tensão Máxima')
plt.hlines(latao_tensao_ruptura, 0, latao_def_lim, colors='red', linestyles='--', label='Tensão de Ruptura')


plt.axes().xaxis.set_minor_locator(tck.AutoMinorLocator())
plt.axes().yaxis.set_minor_locator(tck.AutoMinorLocator())
plt.grid(True, which='major', axis='both')
plt.legend(prop={'size': 20})
plt.savefig('./data/output/images/latao.jpg')

# plt.show()