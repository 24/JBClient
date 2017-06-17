#!/usr/bin/python
# coding = utf-8

import re
import requests
from bs4 import BeautifulSoup

class SimpleCrawler:


    # 解析聚币 btc新闻
    def jubiUrl(self):
        jblist = []
        url = "https://www.jubi.com/btc/"
        try:
            header = {
                'User-Agent':
                    'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) '
                    'AppleWebKit/536.26 (KHTML, like Gecko) '
                    'Version/8.0 Mobile/10A5376e Safari/8536.25'
            }
            req = requests.post(url, headers=header)
            print(req.text)
            soup = BeautifulSoup(req.text, 'html.parser')

            list = soup.find_all('li')# todo 优化搜索结构，去掉最后的不合法<li>
            for i in range(len(list)):
                li = list[i]
                if (li.a is not None) and (li.p is not None):
                    title = li.a.string
                    uri = li.a['href']
                    date = li.span.string

                    jbobj = NewsBean(title, uri, date)
                    jblist.append(jbobj)
        except Exception as e:
            print(e)
        return jblist


# 解析后的新闻
class NewsBean:
    def __init__(self,title, uri, date):
        self.title = title
        self.uri = uri
        self.date = date

    def getTitle(self):
        return self.title

    def getUri(self):
        return self.uri

    def getDate(self):
        return self.date

