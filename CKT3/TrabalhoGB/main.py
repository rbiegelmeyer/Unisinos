''' 
    author: Roberto Biegelmeyer
'''

from os import listdir
import matplotlib.pyplot as plt
import pandas as pd

input_path = './input'                                              # Diretorio de arquivos de entrada
output_path = './output'                                            # Diretorio de arquivos de saida
input_filenames = listdir(input_path)                               # Lista arquivos contidos em um diretorio
input_filenames = sorted(input_filenames, key=len)                  # Ordenar a lista para organizar do mesmo modo que no sistema de arquivos
input_filenames = input_filenames[33:34]                            # Filtro de amostras com base em visualizacoes anteriores

for input_filename in input_filenames:                              # Itera todos os arquivos
    input_file_path = input_path + '/' + input_filename             # Constroi caminho relativo do arquivo de entrada

    output_filename = input_filename.replace('i', 'o')              # Modifica nome do arquivo de entrada para um correspondente ao de saida
    output_file_path = output_path + '/' + output_filename          # Constroi caminho relativo do arquivo de saida

    input_filename = input_filename.split('.')[0][2:]               # Retira extensao do arquivo e os dois primeiros caracteres
    input_filename = input_filename.replace('p', '.')               # Replace 'p' para '.'
    freq_rad = float(input_filename)                                # Convert String to float
    # freq = freq_rad/(2*pi)                                  

    # print(input_file_path)
    df_input = pd.read_csv(input_file_path, delimiter='\t', 
                            header=None, names=['x','y'])           # Cria dataframe com arquivo de entrada
    plt.plot(df_input['x'], df_input['y'], color='blue', 
             label='Sinal de Entrada (' + str(freq_rad) + 'rad/s)') # Plota x e y de entrada no grafico

    # print(output_file_path)
    df_output = pd.read_csv(output_file_path, delimiter='\t', 
                            header=None, names=['x','y'])           # Cria dataframe com arquivo de saida
    plt.plot(df_output['x'] , df_output['y'],
             color='red', label='Sinal de Saída')                   # Plota x e y de saida no grafico

    plt.axhline(y=7.07, color='green', 
                label='Linha de 70,7%% da intensidade')             # Plot linha horizontal para identificacao da frequencia de corte

    # plt.title(str(freq_rad) + ' radianos')                          # Title
    plt.legend(loc='lower right')                                   # Aplicacao de legendas
    plt.xlabel('Tempo (s)')
    plt.ylabel('Tensão (V)')
    plt.grid()                                                      # Grid
    plt.savefig('imagens/' + str(freq_rad) + '.png')
    # plt.show()                                                    # Show
    