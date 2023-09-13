import requests
import json

cotacoes_btc = requests.get('https://economia.awesomeapi.com.br/BTC-BRL/200?start_date=20200101&end_date=20201031')

btc_dic = cotacoes_btc.json()
print(btc_dic)
lista_cotacoes_btc = [item['bid'] for item in btc_dic]
print(lista_cotacoes_btc)