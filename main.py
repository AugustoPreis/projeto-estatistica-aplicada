import pandas as pd
import numpy as np

def valores(pdArray):
  return '{ ' + ', '.join(pdArray.values.astype(str)) + ' }'

def calculaMedia(pdArray):
  return np.mean(pdArray)

def calculaMediana(pdArray):
  return np.median(pdArray)

def calculaModa(pdArray):
  return pdArray.mode().iloc[0]

def calculaAmplitude(pdArray):
  return np.ptp(pdArray)

def calculaDesvioPadrao(pdArray):
  return np.std(pdArray).round(2)

def calculaVariancia(pdArray):
  return np.var(pdArray).round(2)

colunas = [
  'IN_LABORATORIO_INFORMATICA',
  'IN_COMPUTADOR',
  'IN_DESKTOP_ALUNO',
  'QT_DESKTOP_ALUNO',
  'IN_COMP_PORTATIL_ALUNO',
  'QT_COMP_PORTATIL_ALUNO',
  'IN_INTERNET_ALUNOS',
]

file = pd.read_csv(
  'dados-criciuma.csv',
  sep = ';',
  encoding = 'utf-8',
  usecols = colunas,
)

file.replace(0, pd.NA, inplace=True)

file = file.dropna()

file = file.astype(int)

print('--------------------------------------------')
print('DESKTOPS POR ALUNO')
print('--------------------------------------------')
print(f'Valores: {valores(file["QT_DESKTOP_ALUNO"])}')
print(f'Média: {calculaMedia(file["QT_DESKTOP_ALUNO"])}')
print(f'Mediana: {calculaMediana(file["QT_DESKTOP_ALUNO"])}')
print(f'Moda: {calculaModa(file["QT_DESKTOP_ALUNO"])}')
print(f'Amplitude: {calculaAmplitude(file["QT_DESKTOP_ALUNO"])}')
print(f'Desvio Padrão: {calculaDesvioPadrao(file["QT_DESKTOP_ALUNO"])}')
print(f'Variância: {calculaVariancia(file["QT_DESKTOP_ALUNO"])}')
print('\n')
print('--------------------------------------------')
print('COMPUTADORES PORTÁTEIS POR ALUNO')
print('--------------------------------------------')
print(f'Valores: {valores(file["QT_COMP_PORTATIL_ALUNO"])}')
print(f'Média: {calculaMedia(file["QT_COMP_PORTATIL_ALUNO"])}')
print(f'Mediana: {calculaMediana(file["QT_COMP_PORTATIL_ALUNO"])}')
print(f'Moda: {calculaModa(file["QT_COMP_PORTATIL_ALUNO"])}')
print(f'Amplitude: {calculaAmplitude(file["QT_COMP_PORTATIL_ALUNO"])}')
print(f'Desvio Padrão: {calculaDesvioPadrao(file["QT_COMP_PORTATIL_ALUNO"])}')
print(f'Variância: {calculaVariancia(file["QT_COMP_PORTATIL_ALUNO"])}')