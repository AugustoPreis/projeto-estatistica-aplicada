'''
Projeto da disciplina de estatística aplicada

Alunos:
  - Augusto Preis Tomasi
  - Kauã Machado Grathwohl
  - João Vitor Brogni Vamerlati
  - Arthur Romansini Fernandes
  - Otávio Raupp Júnior

Professor:
  - Maria Emilia Da Silva De Bona Freitas
'''

import pandas as pd

# Colunas necessárias para a análise e interpretação dos dados
columns = [
  # Escola possui laboratório de informática?
  'IN_LABORATORIO_INFORMATICA',

  # Escola possui computadores para uso?
  'IN_COMPUTADOR',
  
  # Escola possui Computadores de mesa em uso pelos alunos?
  'IN_DESKTOP_ALUNO',
  
  # Quantidade de computadores de mesa em uso pelos alunos
  'QT_DESKTOP_ALUNO',
  
  # Escola possui Computadores portáteis em uso pelos alunos?
  'IN_COMP_PORTATIL_ALUNO',
  
  # Quantidade de computadores portáteis em uso pelos alunos
  'QT_COMP_PORTATIL_ALUNO',
  
  # Escola possui internet para os alunos?
  'IN_INTERNET_ALUNOS'
]

# Arquivo importado pelo pandas
file = pd.read_csv(
  # Nome do arquivo a ser importado  
  'dados-criciuma.csv',

  # Separador de colunas usado pelo arquivo
  # Arquivos .CSV normalmente utilizam "," ou ";"
  sep=';',

  # Codificação do arquivo utf-8 aceitas caracteres especiais
  encoding='utf-8',
  
  # Colunas do arquivo que serão utilizadas
  usecols=columns
)

#Remove linhas inválidas
file = file.dropna()