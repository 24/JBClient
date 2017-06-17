#!/usr/bin/python
# coding = utf-8

from crawler.EasyCrawler import SimpleCrawler, NewsBean

easyCrawler = SimpleCrawler()
jblist = easyCrawler.jubiUrl()
for item in jblist:
    print(item.getTitle()+" "+item.getDate())
