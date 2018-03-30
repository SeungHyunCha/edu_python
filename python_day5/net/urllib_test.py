
from urllib import request

# f = request.urlopen('http://www.naver.com')
f = request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=python')

naver = f.read().decode('UTF-8')
print(naver)