import pandas as pd
import yfinance as yf

# Define o símbolo da ação que você quer baixar os dados
symbol = 'PETR3.SA'

# Define o intervalo de data que você quer baixar os dados
start_date = '2021-01-04'
end_date = '2021-04-20'

# Baixa os dados da ação usando o Yahoo Finance
data = yf.download(symbol, start=start_date, end=end_date)

# Imprime os dados
print(data)

# Exibe os últimos 5 registros
# print(data.tail())

# Exibe a média dos preços de fechamento
# print(data['Close'].mean())

# -----------------------

# Explicação linha à linha:

# import pandas as pd: importa a biblioteca Pandas com o apelido "pd".

# import yfinance as yf: importa a biblioteca yfinance com o apelido "yf".

# symbol = 'PETR3.SA': define o símbolo da ação que será baixado os dados como sendo PETR3.SA, que é o código da ação da Petrobras na B3.

# start_date = '2021-01-04': define a data de início do intervalo que será baixado os dados como sendo 04 de janeiro de 2021.

# end_date = '2021-04-20': define a data final do intervalo que será baixado os dados como sendo 20 de abril de 2021.

# data = yf.download(symbol, start=start_date, end=end_date): baixa os dados da ação especificada no intervalo de datas especificado usando a função download() da biblioteca yfinance e atribui o resultado a uma variável chamada "data".

# print(data): imprime todos os dados baixados na tela.
# print(data.tail()): imprime os últimos 5 registros dos dados baixados na tela.
# print(data['Close'].mean()): calcula a média dos preços de fechamento da ação baixados e imprime o resultado na tela.