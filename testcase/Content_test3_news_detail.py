#!/usr/bin/python
# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc,xlrd
import json,time
import global_list
from public_1.sql_search import SQL_SEARCH_1
from public_1.sql_vaffle import SQL_vaffle

sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_version import Version
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from func_requests import FuncRequests
#---------------Hotnews详情页----------------------
class List(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()


    #-----------------Hotnews详情页----------------------------------
    def testcase_001(self):
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.path = Url().test_path()
        self.version = Version().test_version()
        # 路径
        url = Url().test_url()
        self.base_url1 =url + '/news/detail'
        member_id="959"
        i = 959
        #sql = SQL_vaffle ().select_uuid ( i )
        #uuid = '%s' % SQL_SEARCH_1 ().search ( sql )
        #print(uuid)
        payload = {"category": "hotnews", "post_id": "42990"}
        headers = {"device": "android ", "version": "3.7.0", "lang": "en", "timestamp": "1564033489234",
                   "token": "FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg",
                   "uuid": "a5f10151-5685-4432-8c35-7198bc6511c9", "serial-number": "48525687125863258471123568955554", "company": "HUAWEI",
                   "phone-model": "P10", "system-version": "8.0.0"}
        result = requests.post ( self.base_url1, params=payload, headers=headers )
        result = result.json ()
        print ( result )
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")



if __name__ == "__main__":
    unittest.main()