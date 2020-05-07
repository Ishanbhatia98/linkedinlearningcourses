import requests
import json

url = 'http://httpbin.org/json'

datajson = requests.get(url)

jsonobj = datajson.json()

data = json.dumps(jsonobj, indent = 4)

print(data)

for k, v in jsonobj.items():
    print(k, type(k), v)
