#!/usr/bin/python3

import requests
import json

APIKey = 'cb88e221-51ee-4694-9f62-c12319dfefea"'
url = '"https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?'
url_header = 'start-1&limit=5&convert=USD&CMC_PRO_API_KEY='
full_request = url + url_header + APIKey

#api_request = requests.get()
print(full_request)
