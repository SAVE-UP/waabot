#get Crypto price in EUR via Coindesk api
import requests

def getbtcprice():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    btc_price = data["bpi"]["EUR"]["rate"]
    return btc_price
"""
Sample of response from coindesk api
{'time': 
     {
    'updated': 'Oct 7, 2021 16:24:00 UTC',
    'updatedISO': '2021-10-07T16:24:00+00:00', 
    'updateduk': 'Oct 7, 2021 at 17:24 BST'
     },
    'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org',
    'chartName': 'Bitcoin',
    'bpi': {
        'USD': {
            'code': 'USD', 'symbol': '&#36;',
            'rate': '53,765.1783', 
            'description': 'United States Dollar', 
            'rate_float': 53765.1783}, 
        'GBP': {
            'code': 'GBP', 'symbol': '&pound;', 
            'rate': '39,440.1455', 
            'description': 'British Pound Sterling', 
            'rate_float': 39440.1455}, 
        'EUR': {'code': 'EUR', 'symbol': '&euro;',
                'rate': '46,508.0083', 
                'description': 'Euro', 
                'rate_float': 46508.0083
                }
    }
}
"""