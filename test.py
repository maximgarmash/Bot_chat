import json
import requests


url = 'https://api.coinmarketcap.com/v1/ticker/'
res = requests.get(url).json()
print(res)
res_json = json.dumps(res, indent=2)
print(type(res_json))
