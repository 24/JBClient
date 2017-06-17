#!/usr/bin/python
# coding = utf-8

from wx.wxApi import WebWeixin

# 微信相关api调用

webwx = WebWeixin()
webwx.start()
webwx.sendMsg()
