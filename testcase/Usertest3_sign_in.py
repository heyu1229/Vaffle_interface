# -*- coding:UTF-8 -*-
import unittest
import requests
import time,gc,sys
import global_list
from public_1.get_url import Url
from public_1.get_version import Version

sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#-----------------------用户登录接口---------------------------
class SignIn(unittest.TestCase):

    def setUp(self):
        self.member_id = 'none'
        self.requests = FuncRequests()



    # -----------------用nickname登录成功--------------------------------
    def testcase_002(self):
        sheet_index =0
        row = 26
        print("testcase002 用nickname登录成功：")
        payload = {"account":"test","password":"111111"}
        urlpart = '/sign/in'
        result1 = self.r.interface_requests_data(959, urlpart, payload)
        # 路径
        url = Url().test_url()
        self.base_url=url+urlpart
        # 获取版本
        self.version = Version().test_version()
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": "1493780505", "token": "FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg",
                   "login": "959","serial-number":"48525687125863258471123568955554","company":"HUAWEI","phone-model":"P10","system-version":"system_version"}
        r = requests.post(self.base_url, params=payload, headers=headers)
        result = r.json()
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")



if __name__ == '__main__':
    unittest.main()
    











