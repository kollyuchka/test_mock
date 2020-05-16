
import requests
import json

url = "http://127.0.0.1:5000/save"

r = requests.get(url)

# print(r.headers)
#
# print(r)

data = {'account' : 1294567,'counter': 23, 'date': '14.05.2020'}



foo = requests.post(url,  data=json.dumps(data))

print(foo.text)
