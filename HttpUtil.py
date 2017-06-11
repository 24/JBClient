#!/usr/bin/python
# coding = utf-8

import http.client
import urllib
import json
import time



def buildParam(key, value):
    param = {
        'amount': 1,
        'price' : 10000,
        'type'  : 'buy',
        'nonce' : 141377098123,
        'key'   : '5zi7w-4mnes-swmc4-egg9b-f2iqw-396z4-g541b',
        'signature': '459c69d25c496765191582d9611028b9974830e9dfafd762854669809290ed82'
    }

    build = urllib.parse.urlencode(param)+"&"+key+"="+value
    return build

def httpGet(url,resource,params=''):
    conn = http.client.HTTPSConnection(url, timeout=10)
    conn.request("GET",resource + '?' + params)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    return json.loads(data)

def httpPost(url,resource,params):
     headers = {
            "Content-type" : "application/x-www-form-urlencoded",
     }
     conn = http.client.HTTPSConnection(url, timeout=10)
     temp_params = urllib.parse.urlencode(params)
     conn.request("POST", resource, temp_params, headers)
     response = conn.getresponse()
     data = response.read().decode('utf-8')
     params.clear()
     conn.close()
     return data