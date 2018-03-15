from requests import get
from bs4 import BeautifulSoup

key= raw_input("Enter a word :")

url ='http://www.dictionary.com/browse/'+key

response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
pos= html_soup.find_all('span', class_ = 'dbox-pg')
definations= html_soup.find_all('div', class_ = 'def-content')
#print(len(definations))
print(pos[0].text)
i=0
while i<3:
    d = definations[i]
    print(d.text)
    i=i+1
    


