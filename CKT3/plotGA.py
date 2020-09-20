#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Ferramenta de plot Análise de Circuitos no Domínio da Frequência - Trabalho GA.
    Gráfico é construido a partir de um arquivo csv de pontos extraído do LTSpice.
"""

__author__: "Roberto Biegelmeyer"
__email__: "rbiegelmeyer@edu.unisinos.br"
# create: 09/18/20

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

df = pd.read_csv('points.csv', delimiter='\t')                                      # interpreta o csv para um df pandas S2
scal = 1e09                                                                         # Reitra a escala de Nanosecond, cabe a interpretacao do usuario agora

ax = plt.gca()
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))                             # Muda o major step vertical
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))                               # muda o major step horizontal
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))                            # muda o minor step horizontal

df['time'] = df['time'] * scal

df.plot(kind='line', x='time', y='V(vin)', label='Vin(V)', ax=ax)                   # plota um relaçao de duas colunas no gráfico
df.plot(kind='line', x='time', y='V(vout)', label='Vout(V)', ax=ax, color='green')  # plota um relaçao de duas colunas no gráfico

plt.xlabel('Tempo (ns)')                                                            # label horizontal
plt.xlim(-0.1,12)                                                                   # limita o plano horizontal para ficar menor
plt.ylabel('Tensão (V)')                                                            # label vertical
plt.ylim(0,1.1)                                                                     # limita o plano vertical para ficar menor

df_temp = df[df['V(vout)'] >= 0.9]                                                  # filtro o df para as linhas que possuem um valor de tensao maior que 0.9
subiu09 = df_temp.iloc[0]                                                           # extraio o primeiro elemento da resultante acima (t1)
desceu09 = df_temp.iloc[-1]                                                         # e extraio o ultimo elemento (t2)

plt.scatter(subiu09['time'], 0.9, color ='black', zorder=99, s=10)                  # ponto preto do t1
plt.scatter(desceu09['time'], 0.9, color ='black', zorder=99, s=10)                 # ponto preto do t2

plt.hlines(0.9, 0, subiu09['time'], color='red', linestyle=':', label='0,9V')       # primeira parte linha vermelha
plt.hlines(0.9, subiu09['time'], desceu09['time'], color='black', linestyle='--')   # linha preta
plt.hlines(0.9, desceu09['time'], 20, color='red', linestyle=':')                   # segunda parte linha vermelha

ax.annotate(
    '', 
    xy=(subiu09['time'], 0.8),
    xycoords='data',
    xytext=(desceu09['time'], 0.8), textcoords='data',
    arrowprops=dict(arrowstyle="<|-|>",shrinkA=0, shrinkB=0)
)                                                                                   # Seta de distancia do t1 para o t2

# tempo_de_pulso = desceu09['time'] - subiu09['time']                               # diferenca de tempo entre o t2 e t1
# ax.text(4.7,0.82, '{:.5}ns'.format(tempo_de_pulso))                               # formata e plota uma string do tempo do pulso

ax.text(1.5, 0.84, 't1')                                                            # plota t1 como text
ax.text(desceu09['time'] + 0.2, 0.84, 't2')                                         # plota t2 como text
ax.text(4.7,0.82, 'tpulso' )                                                        # plota tpulso como text

plt.legend(loc='best')                                                              # aloca a legenda em um lugar melhor
plt.grid(linestyle=':')                                                             # mudança do estilo das linhas do grid

plt.show()                                                                          # hora do show