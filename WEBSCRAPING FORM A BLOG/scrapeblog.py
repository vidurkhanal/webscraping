from bs4 import BeautifulSoup
import requests
import csv

source_code = requests.get('https://coreyms.com').text

soup = BeautifulSoup(source_code,'lxml')

csv_document = open('scraped_data.csv','w')
csv_writer=csv.writer(csv_document)
csv_writer.writerow(['Headline','Summary','Tutorial Link','Published Date','Author'])

articles = soup.find_all('article')
for article in articles:
    article_headline = article.header.h2.a.text
    article_date = article.header.p.time.text
    article_author = article.header.p.span.a.span.text

    summary = article.find('div', class_='entry-content').p.text
    print(article_headline)
    print(summary)

    if article.iframe:
        embedded_link = article.find('iframe', class_='youtube-player')['src']
        video_id = embedded_link.split('/')[4].split('?')[0]
        yt_link = f'https://www.youtube.com/watch?v={video_id}'
    else:
        yt_link = None
    print(f'Tutorial Link:{yt_link}')

    print()

    csv_writer.writerow([article_headline,summary,yt_link,article_date,article_author])



