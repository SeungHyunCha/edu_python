
from bs4 import BeautifulSoup
import urllib.request as req

url = 'http://www.ericssonlg.com/site/ericssonlg/menu/38.do'
response = req.urlopen(url)
soup = BeautifulSoup(response, "html.parser")

tds = soup.select('.board_list  .pt-board-list-row')
print(len(tds))

for td in tds:
    td = td.select('.pt-a')[0].string
    print(td.strip())