# beautifulsoup 4 로 다음 뉴스 "감자 가격" 정보 찾기 (20180101~20181231)
import requests
from bs4 import BeautifulSoup
import time


# url 로 request(요청)
url = 'https://search.daum.net/search?nil_suggest=btn&w=news&DA=STC&cluster=y&q=%EA%B0%90%EC%9E%90+%EA%B0%80%EA%B2%A9&sd=20180101000000&ed=20181231235959&period=u'
response = requests.get(url).text.strip()
# 응답
soup = BeautifulSoup(response, "html5lib")
newslink = soup.select(".coll_cont ul li a.f_link_b")
for link in newslink:
    # 기사를 가져옴
    url_article = link.get('href')
    response = requests.get(url_article).text.strip()
    soup_article = BeautifulSoup(response, "html5lib")
    content = soup_article.select_one("#harmonyContainer")
    print(content.contents)
    # 가공
    output = ""
    for item in content.contents:
        output += str(item)
    print(output)
    # 1초 휴식
    time.sleep(1)
