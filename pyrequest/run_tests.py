#-*- coding:utf-8 -*-
import HTMLTestRunner,time,os,unittest,sys
currentpath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(currentpath)
from interface.add_event_test import AddEventTest,TestInt
#from pyrequest.interface.add_event_test import AddEventTest,TestInt
now=time.strftime("%Y-%m-%d %H-%M-%S",time.localtime())

path=os.path.dirname(os.path.abspath(__file__))+"\\report"+"\\%s.html"%now
print path
suite=unittest.TestSuite()
suite.addTests(unittest.makeSuite(AddEventTest))
suite.addTests(unittest.makeSuite(TestInt))
#suite.addTests(unittest.makeSuite(TestInt))
fp=open(path,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'发布会添加自动化测试报告',description=u'用例执行结果')
runner.run(suite)
#HTMLTestRunner 发布