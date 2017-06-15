#!/usr/bin/python
# coding = utf-8

import urllib

from util.HttpUtil import httpJsonGet


class JuBiSpot:
    def __init__(self, url):
        self.__url = url


# 封装请求的参数
    def buildParam(self, req):
        param = {
            'amount': 1,
            'price': 10000,
            'type': 'buy',
            'nonce': 141377098123,
            'key': '5zi7w-4mnes-swmc4-egg9b-f2iqw-396z4-g541b',
            'signature': '459c69d25c496765191582d9611028b9974830e9dfafd762854669809290ed82'
        }
        build = {'param': urllib.parse.urlencode(param)}

        for key in req:
            build[key] = req[key]
        build = urllib.parse.urlencode(build)
        return build

# 牌价
    def ticker(self, param):
        ticker_api = "/api/v1/ticker/"
        request = {"coin": param}
        return httpJsonGet(self.__url, ticker_api, self.buildParam(request))


# 市场深度
    def depth(self, param):
        ticker_api = "/api/v1/depth/"
        request = {"coin": param}
        return httpJsonGet(self.__url, ticker_api, self.buildParam(request))


# 市场交易
    def orders(self, param):
        ticker_api = "/api/v1/orders/"
        request = {"coin": param}
        return httpJsonGet(self.__url, ticker_api, self.buildParam(request))