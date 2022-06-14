import pandas_datareader as web
from datetime import date, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json

def carteira(n_dias):
    carteira_df = pd.read_excel("carteira.xlsx")
    carteira_df.head()

    today = date.today()
    days_ago = today - timedelta(n_dias)

    total = ''

    for acao in carteira_df['Carteira']:
        df = web.DataReader(
            f'{acao}', data_source='yahoo', start=days_ago, end=today
        )
        acoes = (
            acao
            + '\n'
            + 'Fechamento ajustado de hoje: '
            + str(round(df.iloc[-1][-1], 2))
            + '\nFechamento ajustado mínimo dos últimos '
            + str(n_dias)
            + ' dias: '
            + str(round(df['Adj Close'].min(), 2))
            + '\nFechamento ajustado médio dos últimos '
            + str(n_dias)
            + ' dias: '
            + str(round(df['Adj Close'].mean(), 2))
            + '\nFechamento ajustado máximo dos últimos '
            + str(n_dias)
            + ' dias: '
            + str(round(df['Adj Close'].max(), 2))
            + '\n'
        )
        total += acoes + '\n'
    return total

def moeda():
    moeda = requests.get(
        "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    )
    moeda = moeda.json()
    cotacao_dolar = round(pd.to_numeric(moeda['USDBRL']['bid']), 2)
    cotacao_euro = round(pd.to_numeric(moeda['EURBRL']['bid']), 2)
    cotacao_bitcoin = round(pd.to_numeric(moeda['BTCBRL']['bid']), 2)
    moedas = (
        'Cotação do Dólar: '
        + str(cotacao_dolar)
        + '\nCotação do Euro: '
        + str(cotacao_euro)
        + '\nCotação do Bitcoin: '
        + str(cotacao_bitcoin)
        + '\n'
    )
    return moedas

print(carteira(30), moeda())