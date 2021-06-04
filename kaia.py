import re
import html
import feedparser
from datetime import datetime
from datetime import timedelta



# 오늘 날짜 및 이전 날짜  
current = datetime.today()
prev = current - timedelta(1)        #   이전 날짜부터 조회( timedelta(~일 전))




# kaia rss
rssurl = 'http://hub.kaia.re.kr/rss/techmap.xml'


# rss의 entries만 추출
feed = feedparser.parse(rssurl)
articles = feed.entries 
articles = html.unescape(articles)


kaialist = []

for article in articles:
    date_str = article.published
    date = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %z")
    if str(prev) < str(date):  
        text = article.description
        text = re.sub("<br />", "\n", text)
        text = re.sub("<.*?div>", "\n\n", text)
        text = re.sub("<.*?>", "", text)
        kaialist.append({"title" : html.unescape(article.title), 
                        "description" : html.unescape(text).replace("？", ""),
                        "link" : article.link,
                        "pdate" : str(date).replace("+09:00",""),
                        "published" : article.published})

kaialist.reverse()
for kaia in kaialist:
    print(kaia)
