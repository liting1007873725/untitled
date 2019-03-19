#-*- coding:utf-8 -*-
import unittest,requests,sys
import os, sys,json
parentdir = str(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parentdir)
from parameterized import parameterized
from pyrequest.dbfix import test_data
import unittest,requests
class AddEventTest(unittest.TestCase):
    # @parameterized.expand([
    #     ('11', '红米Pro发布会', '2000','1', '北京会展中心', '2019-8-10 12:30:00'),('111', '红米Pro发布1会', '2000','1', '北京会展中心', '2019-8-10 12:30:00')
    # ])

    def setUp(self):
        self.url='http://127.0.0.1:8000/api/add_event/'

    # def test_add_event_name_exist(self, id, name, linit, status, address, strat_time):
    #     print "data", id, name
    #     data = {'eid':id,'name':name,'linit':linit,'status':status,'address':address,'start_time':strat_time}

        # respone=requests.post(self.url,data=data)
        # self.result=respone.json()
        #print "self.result", self.result
        # self.assertEqual(self.result['status_code'], 203)
        # self.assertEqual(self.result['message'],u'发布会名称已经存在了')
    # def test_field_is_null(self,name1,eid,name,linit,status,address,start_time):
    #     data={'eid':eid,'name':name,'linit':linit,'status':status,'address':address,'start_time':start_time}
    #     respone=requests.post(self.url,data=data)
    #     self.result=json.loads(respone.content)\\
    #     print "ewrwerwe",self.result.keys()
    #     self.assertEqual(self.result['status_code'],201)
    #     self.assertEqual(self.result['message'], u'字段不能为空')
    # @unittest.skip("test_add_event_eid_exist")
    def test_add_event_eid_exist(self):
        data = {'eid': '1', 'name': '11', 'linit': '11', 'status': '0', 'address': '11', 'start_time': '2017-08-20 14:00:00'}
        respone = requests.post(self.url, data=data)
        self.result = respone.json()
        self.assertEqual(self.result['status_code'], 202)
        self.assertEqual(self.result['message'], u'id已经存在了')
import unittest
import math

class TestInt(unittest.TestCase):
    @parameterized.expand([
        ('1',2, 3, 5),('2',3, 5, 8),
    ])
    def test_add(self,name,a, b, expected):
        self.assertEqual(a+b,expected)
        print "aa",a,b
if __name__=="__main__":
    unittest.main()
