"""
daum news d의 링크!! 소리질러~~ %_%
"""
import requests
from bs4 import BeautifulSoup
import time
import datetime

query = "감자가격"
page  = 1

for i in range(1, page+1):
    url = "https://search.daum.net/search?w=news&sort=recency&q={}&cluster=n&DA=STC&s=NS&a=STCF&dc=STC&pg=1&r=1&p={}&rc=1&at=more&sd=&ed=&period="
    real_url = url.format(query, i)
    news = requests.get(real_url)
    news_bs = BeautifulSoup(news.content, 'lxml')
    news_list = news_bs.find_all('div', class_="cont_inner")

    for i in range(len(news_list)):
        print(news_list[i].find('a').text)
        link = news_list[i].find('a')
        print(link.get('href'))
        print("=" * 60)
        url_article = link.get('href')
        news = requests.get(url_article).text.strip()
        news_bs = BeautifulSoup(news, "html5lib")
        content = news_bs.select_one("#harmonyContainer")  # hum .. 언론사마다 HTML 구조 다르다.


