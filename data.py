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
