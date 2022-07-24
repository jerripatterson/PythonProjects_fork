import requests
import json
import os
#os.system('cls')
api_request = requests.get(
    "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=cb88e221-51ee-4694-9f62-c12319dfefea")
apikey = "cb88e221-51ee-4694-9f62-c12319dfefea"
api = json.loads(api_request.content)
#print(api)

currencies = ['BTC', 'XRP', 'EOS', 'STEEM']
for sym in api:
    for coin in currencies:
        if coin == sym['symbol']:
            print(sym['name'])
