#!/usr/bin/python
# coding = utf-8
import time
import random
import re
import qrcode

from HttpUtil import httpPost, httpGet

class WxBot:
    def __init__(self):
        self.url = "login.weixin.qq.com"
        self.uuid = ""
        self.redirect_uri = ""
        self.base_uri = ""
        self.base_host = ""


    # 格式化wx 字符串
    def stringFormat(self, url):
        param = re.search(r'window.code=(\d+);', url)
        code = param.group(1)
        return code

    # 获取uuid
    def uuidGet(self):
        uuid_api = "/jslogin"
        params = {
            'appid': 'wx782c26e4c19acffb',
            'fun': 'new',
            'lang': 'zh_CN',
            '_': int(time.time()),
        }

        uuidstr = httpGet(self.url, uuid_api, params)
        regular = r'window.QRLogin.code = (\d+); window.QRLogin.uuid = "(\S+?)"'
        search = re.search(regular, uuidstr)
        if search:
            code = search.group(1)
            self.uuid = search.group(2)


    # 生成二维码
    def qrcodeGet(self):
        string = 'https://login.weixin.qq.com/l/' + self.uuid
        qrimg = qrcode.make(string)
        qrimg.show()

    # 扫描二维码
    def qrcodeScan(self):
        SCANED = "201"
        SUCCESS = "200"
        TIMEOUT = "408"
        retry_time = 10  # 最大重置登录次数


        scan_api = "/cgi-bin/mmwebwx-bin/login"
        # 扫描状态 1:未扫描 0:已扫描
        tip = 1
        param = {
            "tip": tip,
            "uuid": self.uuid,
            "_": int(time.time())
        }


        while retry_time > 0:
            param["tip"] = tip
            string = httpGet(self.url, scan_api, param)
            code = self.stringFormat(string)

            if code == SUCCESS:
                print(string)
                param = re.search(r'window.redirect_uri="(\S+?)";', string)
                redirect_uri = param.group(1) + '&fun=new'
                self.redirect_uri = redirect_uri
                self.base_uri = redirect_uri[:redirect_uri.rfind('/')]
                temp_host = self.base_uri[8:]
                self.base_host = temp_host[:temp_host.find("/")]
                return code
            elif code == SCANED:
                tip = 0
            elif code == TIMEOUT:
                tip = 1  # 重置
                retry_time -= 1
                time.sleep(5)
            else:
                tip = 1
                retry_time -= 1
                time.sleep(5)


    #  登录获取Cookie
    def login(self):
        string = httpGet(self.url, scan_api, param)


