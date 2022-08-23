#!/usr/bin/python3

import requests
import json

APIKey = 'cb88e221-51ee-4694-9f62-c12319dfefea"'
url = '"https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?'
url_header = 'start-1&limit=5&convert=USD&CMC_PRO_API_KEY='
api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest/")
#print(api_request)

api =  json.loads(api_request.content)

print(api)
