import requests

r = requests.get('http://www.cnydsimtek.com/company')

print(r.text)
