from bs4 import BeautifulSoup
import urllib.request as req

url = 'http://www.chosun.com/site/data/rss/rss.xml'
response = req.urlopen(url)
soup = BeautifulSoup(response, "html.parser")

items = soup.select('item')
for item in items:
    title = item.select('title')[0].string
    print(title)