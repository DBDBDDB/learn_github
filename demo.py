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
    imageURL = soup.find_all('img', attrs={"data-src": True})
    
    imageList = []
    for i in imageURL:
        imageList.append(i['data-src'])
    return imageList[0:3]


def saveImage(imageURL):
    m = 1
    for i in imageURL:
        imageData = requests.get("http:"+i)
        with open(str(m)+'.jpg', 'wb') as f:
            f.write(imageData.content)
            m = m+1


def main():
    url = "http://www.cnydsimtek.com/company"
    data = getHTML(url)
    imageURL = parserHTML(data)
    saveImage(imageURL)


main()
