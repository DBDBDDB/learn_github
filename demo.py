import requests
from bs4 import BeautifulSoup


def getHTML(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r
    except:
        return ""


def parserHTML(data):
    soup = BeautifulSoup(data.text, 'html.parser')
    imageURL = soup.find('img', attrs={"data-src": True})
    return imageURL['data-src']


def saveImage(imageURL):
    imageData = requests.get('http:'+imageURL)
    with open('Dr-Ji.jpg', 'wb') as f:
        f.write(imageData.content)


def main():
    url = "http://www.cnydsimtek.com/company"
    data = getHTML(url)
    imageURL = parserHTML(data)
    saveImage(imageURL)


main()
