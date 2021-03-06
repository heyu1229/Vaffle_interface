#!/usr/bin/python
# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,gc
import xlrd

import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
from get_version import Version
from func_requests import FuncRequests

#---------------用户关注列表----------------------
class Following(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------我关注的用户列表----------------------------------
    def testcase_001(self):
        sheet_index = 2
        row = 6
        print("testcase_001我关注的用户列表：")
        member_id = "744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")


    # -----------------进入其他用户主页查看该用户关注的列表----------------------------------
    def testcase_002(self):
        sheet_index = 2
        row = 7
        print("testcase_002进入其他用户主页查看该用户关注的列表:")
        member_id="744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

    #-----------------关注列表为空或者用户不存在----------------------------------
    def testcase_003(self):
        sheet_index = 2
        row = 8
        print("testcase_003关注列表为空或者用户不存在")
        member_id="744"
        result=self.r.interface_requests(member_id,sheet_index,row)

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__=="__main__":
    unittest.main()