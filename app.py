#!/usr/bin/env python3
import pyautogui
import time
import pandas as pd
import os
pyautogui.PAUSE = 0.5

flag = True
# Recebendo os aquivo do usuario
file_name = str(input('Nome da aquiivo txt vazio:'))
fold = str(input('Nome onde o aquivo csv esta: '))


# Verifica se arquivo CSV
if os.path.isfile(file_name):

    print('Todos os dados já estão em neste arquivo txt crie outro')
    exit()
    


# Lendo os arquivo
try:
    tabela = pd.read_csv(fold)
except FileNotFoundError:
    flag = False
    print(f'O Arquivo não foi econtrado em {fold}')
    


if flag == False:
    print('ALGO DEU ERRADO... ')
    print('1: DIGITE CRIE UM ARQUIVO.txt\nDEPOIS DIGITE O LOCAL ONDE ESTA O ARQUIVO CSV ')

if flag == True:
    output_file = file_name

with open(output_file,'w') as arquivo:

    for line in tabela.index:
    
        codigo = str(tabela.loc[line, 'codigo'])
        marca = str(tabela.loc[line, 'marca'])
        tipo = str(tabela.loc[line, 'tipo'])

        time.sleep(0.3)

        categoria = str(tabela.loc[line, 'categoria'])
        preco = str(tabela.loc[line, 'preco_unitario'])
        time.sleep(0.3)
        
        custo = str(tabela.loc[line, 'custo'])

        arquivo.write(f'codigo: {codigo}, marca: {marca}, tipo: {tipo}, categoria: {categoria}, preço: {preco}, custo: {custo}\n')
  



print(f'Arquivo salvo em {output_file}')

