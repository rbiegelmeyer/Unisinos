''' 
    author: Roberto Biegelmeyer
'''

from os import listdir
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import pandas as pd
from math import pi, log10
from scipy import signal, fftpack
import numpy as np

# Frequency (rad/s)', 'Magnitude (dB)', 'Phase (deg)'
df_total = pd.DataFrame(columns = ['frequency', 'magnitude', 'phase'])

input_path = './input'                                          # Diretorio de arquivos de entrada
output_path = './output'                                        # Diretorio de arquivos de saida
input_filenames = listdir(input_path)                           # Lista arquivos contidos em um diretorio
input_filenames = sorted(input_filenames, key=len)              # Ordenar a lista para organizar do mesmo modo que no sistema de arquivos
# input_filenames = input_filenames[20:43]                               # Filtro de amostras com base em visualizacoes anteriores

for input_filename in input_filenames:                          # Itera todos os arquivos
    input_file_path = input_path + '/' + input_filename         # Constroi caminho relativo do arquivo de entrada

    output_filename = input_filename.replace('i', 'o')          # Modifica nome do arquivo de entrada para um correspondente ao de saida
    output_file_path = output_path + '/' + output_filename      # Constroi caminho relativo do arquivo de saida

    input_filename = input_filename.split('.')[0][2:]           # Retira extensao do arquivo e os dois primeiros caracteres
    input_filename = input_filename.replace('p', '.')           # Replace 'p' para '.'
    freq_rad = float(input_filename)                            # Convert String to float
    freq = freq_rad/(2*pi) 

    df_input = pd.read_csv(input_file_path, delimiter='\t', 
                            header=None, names=['x','y'])       # Cria dataframe com arquivo de entrada
    df_output = pd.read_csv(output_file_path, delimiter='\t', 
                            header=None, names=['x','y'])       # Cria dataframe com arquivo de saida

    x = df_input['x']
    y1 = df_input['y']
    y2 = df_output['y']

    # Plot
    # plt.plot(df_input['x'], y1,
    #          color='blue', label='Sinal de Entrada')            # Plota x e y de entrada no grafico
    # plt.plot(df_output['x'] , y2,
    #          color='red', label='Sinal de Saída')               # Plota x e y de saida no grafico
    # plt.title(str(freq_rad) + ' radianos')                      # Title
    # plt.legend(loc='upper right')                               # Aplicacao de legendas
    # plt.grid()                                                  # Grid
    # plt.show()                                                  # Show

    # Gain
    peak_y1 = y1.max()                                          # Extrai maior amplitude da serie de entrada
    peak_y2 = y2.max()                                          # Extrai maior amplitude da serie de saida
    gain = peak_y2/peak_y1                                      # determina uma relacao de ganho
    gain_db = 20 * log10(gain)                                  # dB
    # print('Ganho({}rad/s): {}'.format(freq_rad, gain_db))

    # Phase
    zero_crossings = np.where(np.diff(np.sign(y1)))[0]          # Determina os zero crossing
    dot_period = zero_crossings[1] - zero_crossings[0]          # Diferenca entre um e outro determina periodo


    xcorr = signal.correlate(y1.tolist(), y2.tolist())          # Correlaciona um sinal ao outro para determinar os cruzamentos
    dot_delay = 999 - xcorr.argmax()                            # Determina o delay de um sinal com outro atraves
    phase = - (float(dot_delay) / float(dot_period)) * (180)    # Determina a defasagem de sinal  
    # print('Delay: {} \nPeriod: {} \nPhase: {}'.format(dot_delay, dot_period, phase))

    row = {
        'frequency': str(int(freq_rad)),
        'magnitude': round(gain_db, 2),
        'phase': round(phase, 2)
        }                                                       # Cria row para inserir no df
    df_total = df_total.append(row, ignore_index=True)          # Insere row no dataframe


df_total.to_csv(r'save.csv')                                    # Salva dataframe em um arquivo csv

freqs = df_total['frequency']                                   # Extrai serie de frequencias
mags = df_total['magnitude']                                    # Extrai serie de magnitudes
phases = df_total['phase']                                      # Extrai serie de phases

# Plot Bode
plt.figure()
plt.semilogx(freqs, mags, color='black')                        # Bode magnitude plot
plt.scatter(freqs, mags, color='black')
plt.title('Frequency x Magnitude')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Magnitude (dB)')
plt.axvline(x=7000, color='black', linestyle=':')
plt.axhline(y=-3, color='black', linestyle=':')
plt.axes().yaxis.set_minor_locator(tck.AutoMinorLocator())
plt.grid(True, which='major', axis='y')
plt.grid(True, which='both', axis='x')
plt.savefig('imagens/freqXmag_1.png')

plt.figure()
plt.semilogx(freqs, phases, color='black')                      # Bode phase plo
plt.scatter(freqs, phases, color='black')
plt.title('Frequency x Phase')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Phase (deg)')
plt.axvline(x=7000, color='black', linestyle=':')
plt.axhline(y=-45, color='black', linestyle=':')
plt.axes().yaxis.set_minor_locator(tck.AutoMinorLocator())
# plt.yticks(np.arange(-90,5,10))
plt.grid(True, which='major', axis='y')
plt.grid(True, which='both', axis='x')
plt.savefig('imagens/freqXpha_1.png')

# plt.show()                                                      # Show
 