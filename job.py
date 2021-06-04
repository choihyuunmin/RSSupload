import re
import html
import feedparser
from datetime import datetime
from datetime import timedelta



# 오늘 날짜 및 이전 날짜  
current = datetime.today()
prev = current - timedelta(11)        #   이전 날짜부터 조회( timedelta(~일 전))


# 국토부뉴스 rss
rssurl = 'http://hub.kaia.re.kr/rss/hire.xml'


# rss의 entries만 추출
feed = feedparser.parse(rssurl)
articles = feed.entries 
articles = html.unescape(articles)


joblist = []

for article in articles :
    date_str = article.published
    date = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %z")
    if str(prev) < str(date):
        text = article.description
        text = re.sub("<.*?br.*?>", "\n\n", text)
        # text = re.sub("<b>", "\n", text)
        # text = re.sub("<.*?>", "", text)
        joblist.append({"title" : html.unescape(article.title), 
                        "description" : html.unescape(text).replace("？",""),
                        "link" : article.link,
                        "pdate" : str(date).replace("+09:00",""),
                        "published" : article.published})

joblist.reverse()
for job in joblist:
    print(job)
