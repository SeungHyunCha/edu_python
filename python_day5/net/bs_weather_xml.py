from bs4 import BeautifulSoup
import urllib.request as req

url = 'http://www.weather.go.kr/wid/queryDFSRSS.jsp?zone=1150060300'
response = req.urlopen(url)
soup = BeautifulSoup(response, "html.parser")

category = soup.select('category')[0].string

print(category)

datas = soup.select('data')

# print(datas)
for data in datas:
    print(data.hour, data.hour.name, data.hour.string, data.hour.parent.name, data['seq'])

