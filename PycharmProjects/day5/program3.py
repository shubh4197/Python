from requests import get
from bs4 import BeautifulSoup
url='http://www.moneycontrol.com'
response=get(url)
soup=BeautifulSoup(response.text,'html.parser')
print(response.text)
print(type(soup))
print(soup.html.head.title)
type(soup)
table=soup.find_all('table',class_="rhsglTbl")
anchor=soup.find_all('a',attrs={'title':''})
links=soup.find_all('a')
#for link in links:
 #   print(link.get('href'))

#print(table)
tables=soup.find_all('table')
for table in tables:
    links=table.find_all('tr')
    for i in links:
            lol=i.find_all('td',class_="grntxt")
            print(lol)
#print(anchor)