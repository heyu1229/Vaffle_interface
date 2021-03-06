# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
# sys.path.append("/usr/lib/python3/heaven_interface_vaffle2.0_auto2/public")
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_version import Version
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from func_requests import FuncRequests

#---------------修改品牌logo----------------------
class Brands(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------修改品牌logo----------------------------------
    # "avatar/1534491048212_1645_android.jpg"
    # "avatar/1534820178727_980_android.jpg"
    def testcase_001(self):
        sheet_index = 11
        row = 6
        member_id='34791'
        print ("testcase_001修改品牌logo:")

        payload = {"brand_id": 1, "logo_url": "avatar/1534491048212_1645_android.jpg"}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()
