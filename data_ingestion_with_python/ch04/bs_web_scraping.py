from bs4 import BeautifulSoup as bs
from datetime import datetime

f = open('fx.html')
html = f.read()

soup = bs(html ,'html.parser')
date = soup.findAll('i' ,{'class':'date'})
print(date[0].contents[0])

currency = soup.findAll('i', {'class':'fas'})
for tr in soup('tr'):
    symbol, value = tr('td')
    #print(symbol('i')[0].attrs)
    #print(symbol.attrs['title'])
    print(symbol('i')[0]['title'], float(value.contents[0]))
