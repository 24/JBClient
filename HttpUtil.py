#!/usr/bin/python
# coding = utf-8

import http.client
import urllib
import json


# http get请求
def httpGet(url, resource, params=''):
    if isinstance(params, dict):
        params = urllib.parse.urlencode(params)

    conn = http.client.HTTPSConnection(url, timeout=10)
    conn.request("GET",resource + '?' + params)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    return data


# http json get请求
def httpJsonGet(url, resource, params=''):
    data = httpGet(url, resource, params)
    return json.loads(data)


# http post请求
def httpPost(url, resource, params):
    if isinstance(params, dict):
        params = urllib.parse.urlencode(params)

    headers = {
            "Content-type": "application/x-www-form-urlencoded",
    }
    conn = http.client.HTTPSConnection(url, timeout=10)
    temp_params = urllib.parse.urlencode(params)
    conn.request("POST", resource, temp_params, headers)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    params.clear()
    conn.close()
    return data


# http json post请求
def httpJsonPost(url, resource, params):
    data = httpPost(url, resource, params)
    return json.loads(data)