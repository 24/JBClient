#!/usr/bin/python
# coding = utf-8

from urllib import request
import re


class SimpleCrawler:
    def __init__(self, url):
        self.url = url

    def testUrl(self):
        try:
            header = {
                'User-Agent':
                    'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) '
                    'AppleWebKit/536.26 (KHTML, like Gecko) '
                    'Version/8.0 Mobile/10A5376e Safari/8536.25'
            }
            req = request.Request(self.url, headers=header)

            reply = request.urlopen(req)
            content = reply.read().decode("utf-8")

            regular = "<div class='content'>[\s\S.]*</div>"
            pattern = re.compile(regular, re.S)
            items = re.findall(pattern, content)
            for item in items:
                print(item[0])
        except Exception as error:
            print(error)


