from bs4 import BeautifulSoup
import urllib.request as req

url = 'http://www.naver.com'
response = req.urlopen(url)
soup = BeautifulSoup(response, "html.parser")

search_list = soup.select('ul.ah_l')
# print(len(search_list))

# search_list = soup.select('ul.ah_l .ah_k')
search_list = soup.select('ul.ah_l span.ah_k')
# print(len(search_list))
# for i in search_list:
#     print(i.string)

search_list = soup.select('ul.ah_l li') #select = tag, . = class

for li in search_list:
    rank = li.select('.ah_r')[0].string #string = text
    key = li.select('.ah_k')[0].string
#     print(rank, key)

search_list = soup.select('.ca_l > .ca_item') # child
for li in search_list:
    print(li.select('a')[0].string)
    print(li.string)