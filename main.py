import requests
from bs4 import BeautifulSoup
r =requests.get('https://quotes.toscrape.com')

soup =BeautifulSoup(r.text, 'html.parser')
print(r.url)
if r.status_code==200:
    print ('success')
    print(soup.title)