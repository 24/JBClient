#!/usr/bin/python
# coding = utf-8

from JubiAPI import JuBiSpot
from WxApi import WxBot

JubiURL = "www.jubi.com"

jubiSpot = JuBiSpot(JubiURL)

print(jubiSpot.ticker("btc"))

print(jubiSpot.depth("btc"))

print(jubiSpot.orders("btc"))

# 微信相关api调用
wxBot = WxBot()
wxBot.uuidGet()
wxBot.qrcodeGet()
wxBot.qrcodeScan()

