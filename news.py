import re
import html
import feedparser
from datetime import datetime
from datetime import timedelta





# 오늘 날짜 및 이전 날짜  
current = datetime.today()
prev = current - timedelta(1)        #   이전 날짜부터 조회( timedelta(~일 전))


# 국토부뉴스 rss
rssurl = 'https://www.korea.kr/rss/dept_molit.xml'


# rss의 entries만 추출
feed = feedparser.parse(rssurl)
articles = feed.entries 
articles = html.unescape(articles)


newslist = []

for article in articles :
    date_str = article.published
    date = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %Z")
    if str(prev) < str(date):
        text = article.description
        text = re.sub("<.*?div>", "\n\n", text)
        text = re.sub("<.*?>", "", text)
        newslist.append({"title" : html.unescape(article.title), 
                        "description" : html.unescape(text).replace("？",""),
                        "link" : article.link,
                        "pdate" : str(date),
                        "published" : article.published})

newslist.reverse()
for news in newslist:
    print(news)
