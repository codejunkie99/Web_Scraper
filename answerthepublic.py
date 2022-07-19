import requests
from bs4 import BeautifulSoup
# Collect and parse first page
page = requests.get('https://answerthepublic.com/reports/5b8d26d8-99aa-4fd0-bae1-47ecbbd58bad')

soup = BeautifulSoup(page.content, 'html.parser')

for hit in soup.find_all('div', class_="columns small-10"): #questions,prepositions,comparison
    info = hit.text
    info = hit.text
    print(info)

for alpha in soup.find_all('ul', class_="modifier-list"):  #alphabets
    info1 = alpha.text
    print(info1)









