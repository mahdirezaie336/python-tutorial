import requests


res = requests.get('http://ping.eu')
print(res.text)
