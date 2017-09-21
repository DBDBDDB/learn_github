import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.cnydsimtek.com/company')
soup = BeautifulSoup(r.text, 'html.parser')
imageURL = soup.find('img', attrs={"data-src": True})
image = imageURL['data-src']

print(image)
