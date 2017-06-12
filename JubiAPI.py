#!/usr/bin/python
# coding = utf-8

from HttpUtil import httpGet, httpPost, buildParam


class JuBiSpot:
    def __init__(self, url):
        self.__url = url


# 牌价
    def ticker(self, param):
        ticker_api = "/api/v1/ticker/"
        request = {"coin": param}
        return httpGet(self.__url, ticker_api, buildParam(request))


# 市场深度
    def depth(self, param):
        ticker_api = "/api/v1/depth/"
        request = {"coin": param}
        return httpGet(self.__url, ticker_api, buildParam(request))


# 市场交易
    def orders(self, param):
        ticker_api = "/api/v1/orders/"
        request = {"coin": param}
        return httpGet(self.__url, ticker_api, buildParam(request))