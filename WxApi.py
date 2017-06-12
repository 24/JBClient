#!/usr/bin/python
# coding = utf-8
import time
import random
import re
import qrcode

from HttpUtil import httpPost

class WxBot:
    def __init__(self):
        self.url = "login.weixin.qq.com"
        self.uuid = ""

# 获取uuid
    def uuidGet(self):
        uuid_api = "/jslogin"
        params = {
            'appid': 'wx782c26e4c19acffb',
            'fun': 'new',
            'lang': 'zh_CN',
            '_': int(time.time()) * 1000 + random.randint(1, 999),
        }

        uuidstr = httpPost(self.url, uuid_api, params)
        regular = r'window.QRLogin.code = (\d+); window.QRLogin.uuid = "(\S+?)"'
        search = re.search(regular, uuidstr)
        if search:
            code = search.group(1)
            self.uuid = search.group(2)
            return code == '200'
        return False


# 生成二维码
    def gen_qr_code(self, qr_file_path):
        string = 'https://login.weixin.qq.com/l/' + self.uuid
        qr = pyqrcode.create(string)
        if self.conf['qr'] == 'png':
            qr.png(qr_file_path, scale=8)
            show_image(qr_file_path)
            # img = Image.open(qr_file_path)
            # img.show()
        elif self.conf['qr'] == 'tty':
            print(qr.terminal(quiet_zone=1))


