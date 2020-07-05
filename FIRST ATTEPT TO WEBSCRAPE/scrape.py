from bs4 import BeautifulSoup
import requests
with open('simplehtml.html') as html_file:
    soup=BeautifulSoup(html_file ,'lxml')

articles= soup.find_all('div' ,class_='article')
for article in articles:
    headline = article.h2.a.text
    print(headline)

    content = article.p.text
    print(content)
    print('\n \n')


