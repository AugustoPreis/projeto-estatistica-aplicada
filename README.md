# Projeto Estatística Aplicada

## Alunos
  - Augusto Preis Tomasi
  - Kauã Machado Grathwohl
  - João Vitor Brogni Vamerlati
  - Arthur Romansini Fernandes
  - Otávio Raupp Júnior

## Objetivos

  - Calcular a média, mediana, moda, amplitude, desvio padrão e variância dos valores
  - O cálculo destes valores deve ser realizado utilizando as bibliotecas `numpy` e `pandas`

## Funcionalidades

Importa as bibliotecas utilizadas
```
import pandas as pd
import numpy as np
```

Lê o arquivo CSV, que deve estar no mesmo diretório do arquivo executado
```
file = pd.read_csv(
  'dados-criciuma.csv',
  sep = ';',
  encoding = 'utf-8',
  usecols = colunas,
)
```

`dados-criciuma.csv` é o arquivo .csv em que as informações foram coletadas

[Neste link](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar) você pode encontrar o arquivo utilizado

`sep = ';'` é o separador utilizado pelo arquivo csv, mais informações [aqui](https://rockcontent.com/br/blog/csv/)

`encoding = 'utf-8'` é a configuração que permite uso de caracteres especiais, como acentos, por exemplo.

`usecols = colunas` são as colunas do csv que desejamos utilizar

Para este projeto, as seguintes colunas serão utilizadas:

```
colunas = [
  'IN_LABORATORIO_INFORMATICA', # Possui laboratório de informática
  'IN_COMPUTADOR', # Possui computadores
  'IN_DESKTOP_ALUNO', # Possui desktops
  'QT_DESKTOP_ALUNO', # Quantidade de desktops por aluno
  'IN_COMP_PORTATIL_ALUNO', # Possui computadores portáteis
  'QT_COMP_PORTATIL_ALUNO', # Quantidade de computadores por aluno
  'IN_INTERNET_ALUNOS', # Possui internet para alunos
]
```

Após importar o arquivo, os seguintes comandos serão realizados

`file.replace(0, pd.NA, inplace=True)` Troca valores inválidos para `pd.NA`, para serem removidos mais tarde

`file = file.dropna()` Remove os valores `pd.NA`, utilizados anteriormente

`file = file.astype(int)` Converte os números para inteiros

### Funções:

Transforma valores como `[1, 2, 3, 4, 5]` em `{1, 2, 3, 4, 5}`, para mostrar em tela
```
def valores(pdArray):
  return '{ ' + ', '.join(pdArray.values.astype(str)) + ' }'
```
#
Calcula a média dos valores, utilizando a função `numpy.mean`
```
def calculaMedia(pdArray):
  return np.mean(pdArray)
```
#
Calcula a mediana dos valores, utilizando a função `numpy.median`
```
def calculaMediana(pdArray):
  return np.median(pdArray)
```
#
Calcula a moda dos valores, utilizando a função `numpy.mode` <br />
A função retorna um objeto, para obter o valor numérico é necessário acessar `.iloc[0]`
```
def calculaModa(pdArray):
  return pdArray.mode().iloc[0]
```
#
Calcula a amplitude dos valores, utilizando a função `numpy.ptp`
```
def calculaAmplitude(pdArray):
  return np.ptp(pdArray)
```
#
Calcula a média dos valores, utilizando a função `numpy.std` <br />
O valor pode ter muitas casas decimais, para evitar estes casos, é utilizado `.round(2)`, arrendondando para 2 casas decimais
```
def calculaDesvioPadrao(pdArray):
  return np.std(pdArray).round(2)
```
#
Calcula a variância dos valores, utilizando a função `numpy.var` <br />
O valor pode ter muitas casas decimais, para evitar estes casos, é utilizado `.round(2)`, arrendondando para 2 casas decimais
```
def calculaVariancia(pdArray):
  return np.var(pdArray).round(2)
```
