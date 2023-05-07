
#Python program to scrape website 
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv


def scrape_paragraphs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    paragraphs = soup.find_all('p')

    return [p.text for p in paragraphs]

   
URL = "https://www.dittapotek.no/c/munn--og-tannpleie/a/A50002"
r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html5lib')
   
quotes=[]  # a list to store quotes

# table = soup.find('div') 
table = soup.find('div', attrs = {'id':'all_quotes'}) 
   
for row in table.findAll('div',
                         attrs = {'class':'js-shortcut-section'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)
   
filename = 'munn2.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)