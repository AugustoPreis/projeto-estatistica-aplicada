import pandas as pd

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

file = file.sort_values(by=['QT_DESKTOP_ALUNO', 'QT_COMP_PORTATIL_ALUNO'])

media = {
  'QT_DESKTOP_ALUNO': file['QT_DESKTOP_ALUNO'].mean(),
  'QT_COMP_PORTATIL_ALUNO': file['QT_COMP_PORTATIL_ALUNO'].mean(),
}

mediana = {
  'QT_DESKTOP_ALUNO': file['QT_DESKTOP_ALUNO'].median(),
  'QT_COMP_PORTATIL_ALUNO': file['QT_COMP_PORTATIL_ALUNO'].median(),
}

moda = {
  'QT_DESKTOP_ALUNO': file['QT_DESKTOP_ALUNO'].mode().iloc[0],
  'QT_COMP_PORTATIL_ALUNO': file['QT_COMP_PORTATIL_ALUNO'].mode().iloc[0],
}

porcentis = {
  # TODO
}

amplitude = {
  'QT_DESKTOP_ALUNO': file['QT_DESKTOP_ALUNO'].max() - file['QT_DESKTOP_ALUNO'].min(),
  'QT_COMP_PORTATIL_ALUNO': file['QT_COMP_PORTATIL_ALUNO'].max() - file['QT_COMP_PORTATIL_ALUNO'].min(),
}

desvioPadrao = {
  'QT_DESKTOP_ALUNO': file['QT_DESKTOP_ALUNO'].std(),
  'QT_COMP_PORTATIL_ALUNO': file['QT_COMP_PORTATIL_ALUNO'].std(),
}

variancia = {
  # TODO
}