#get Crypto price in EUR via Coindesk api

import requests

def getbtcprice():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    btc_price = data["bpi"]["EUR"]["rate"]
    return btc_price

# ToDo Change Coindesk Api for CoinmarketCap Api