#!/usr/bin/python
# coding = utf-8

from HttpUtil import httpGet, httpPost, buildParam


class JuBiSpot:
    def __init__(self, url):
        self.__url = url

    def ticker(self, param):
        ticker_api = "/api/v1/ticker/"
        request = "coin"
        return httpGet(self.__url, ticker_api, buildParam(request, param))