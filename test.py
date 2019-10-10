import json
import requests


url = 'https://api.coinmarketcap.com/v1/ticker/start'
res = requests.get(url).text
print(res)
res_json = json.dumps(res, indent=2)
print(type(res_json))
