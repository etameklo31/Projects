import requests
from bs4 import BeautifulSoup

url = 'https://etsy.com/'
# url = 'https://www.codewithtomi.com/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
title = soup.find_all('span', {'class':'wt-nudge-t-1'})
print(title[1].getText())

# print(r.content)
# look more into webscraping (refer back to video with tomi)