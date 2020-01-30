# 프로토타입
import requests
from bs4 import BeautifulSoup


# url 로 request(요청)
url = 'https://search.daum.net/search?nil_suggest=btn&w=news&DA=STC&cluster=y&q=%EA%B0%90%EC%9E%90+%EA%B0%80%EA%B2%A9&sd=20180101000000&ed=20181231235959&period=u'
html = requests.get(url).text.strip()
# 응답
soup = BeautifulSoup(html, "html5lib")
newslink = soup.select(".coll_cont ul li a.f_link_b")
for link in newslink:
    print(link.get('href'))

# //*[@id="clusterResultUL"]/li[1]/div[2]/div/div[1]/a
# 개발자도구에서 Xpath 찾기 -> 가고자 하는 url 우클릭 -> copy -> Xpath
# '#meign" -> id=meigen이라는 id를 선택
