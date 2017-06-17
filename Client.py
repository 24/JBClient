#!/usr/bin/python
# coding = utf-8

from crawler.EasyCrawler import SCrawler, NewsBean
from wx.wxApi import WebWeixin


crawler = SCrawler()
jblist = crawler.jubiUrl()
