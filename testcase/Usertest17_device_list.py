# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,gc
import global_list
sys.path.append(global_list.path+"/public_1")
from func_requests import FuncRequests
#------------------------用户的电子烟设备列表  vape_member_vape_device表--------1:正常; 0:删除   2:待审核-------------------
class DeviceList(unittest.TestCase):

    def setUp(self):
        self.member_id = '744'
        self.requests = FuncRequests()
    #-----------------用户的电子烟设备列表   pending,not_passed,verified)----------------------------------
    def testcase_001(self):
        sheet_index =0
        row = 64
        print("testcase001 用户的电子烟设备列表：")
        result = self.requests.interface_requests(self.member_id,sheet_index,row)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
        self.assertEqual('', result['msg'])
        print("msg返回值：ok")

if __name__ == '__main__':
    unittest.main()