from bs4 import BeautifulSoup
import requests


print("""Enter A Topic Number To Read Latest News Snippets;
        1.Politics
        2.Valley
        3.Opinion
        4.Sports
        5.Money
        6.National
        7.Culture & Arts
""")

topics = {1: 'politics', 2 : 'valley' , 3 : 'opinion', 4 : 'sports', 5 : 'money', 6 : 'national', 7 : 'art-culture'}

try:
    user_choice = int(input(">>"))
    source_code = requests.get(f'https://kathmandupost.com/{topics[user_choice]}').text

    soup = BeautifulSoup(source_code, 'lxml')

    articles = soup.find_all('article', class_='article-image')
    for sn,article in enumerate(articles, start=1):
        headline = article.h3.text
        author = article.span.a.text
        article_id = article.find('a')['href']
        article_link = f'https://kathmandupost.com{article_id}'
        article_summary = article.p.text
        print(f"""
{sn}. {headline}
                                                                                                          -By {author}

{article_summary}

Want To Read The Full News:
{article_link}

""")

except ValueError:
    print("Please enter the Serial Number of Topic as listed above.")

except AttributeError:
    pass
