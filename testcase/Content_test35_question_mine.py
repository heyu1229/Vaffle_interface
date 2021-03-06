# -*- coding:UTF-8 -*-
import unittest
import requests
import sys
import json
import time

import xlrd

import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_version import Version
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from func_requests import FuncRequests

#---------------用户自己发布的Q／A列表----------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------用户自己发布的Q／A列表第一页数据----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 87
        print("testcase_001 用户自己发布的Q／A列表第一页数据：")

        member_id = "748"
        payload = {"page": 1,"type": "qa","member_id":member_id}

        result=self.r.interface_requests_payload(member_id, sheet_index, row, payload)
        global last_question_id
        last_question_id=result["data"]["last_question_id"]

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    # -----------------用户自己发布的Q／A列表第一页数据-----------------------------------
    def testcase_002(self):
        sheet_index = 1
        row = 88
        print("testcase_002 用户自己发布的Q／A列表第一页数据：")
        member_id = "748"
        payload = {"page": 2, "type": "qa", "member_id": member_id,"last_question_id":last_question_id}
        result = self.r.interface_requests_payload(member_id, sheet_index, row, payload)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()