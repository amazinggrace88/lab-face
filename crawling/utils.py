import datetime

# 원하는 수집기간 정의
def news_datesetting(startday, endday):
    """
    startday : "" 문자열 형태
    endday : "" 문자열 형태이며 실제 날짜보다 하루 더 주어야 한다.

    # https://jeongwookie.github.io/2019/05/31/190531-naver-main-news-crawling/ 참조
    """
    days_range = []

    start = datetime.datetime.strptime(startday, "%Y-%m-%d")
    end = datetime.datetime.strptime(endday, "%Y-%m-%d")
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]

    for date in date_generated:
        days_range.append(date.strftime("%Y-%m-%d"))

    return days_range


if __name__ == '__main__':
    print(news_datesetting("2019-01-01", "2019-12-31"))