#coding:utf-8
import glob
import log,logging
from appium import webdriver
import unittest
import os,sys,time,re
import HTMLTestRunner
from find import *

#logger = log.Logger('rst/log.log',clevel = logging.DEBUG,Flevel = logging.INFO)
def load_tests():
    #logger加到此处eclispe才有日志输出加到这里也可以
 #   logger = log.Logger('rst/log.log',clevel = logging.INFO,Flevel = logging.INFO)
    test_file_strings = glob.glob('test_*.py')    
    module_strings = [str[0:len(str)-3] for str in test_file_strings]
    print module_strings
    suites = [unittest.defaultTestLoader.loadTestsFromName(str) for str in module_strings]
    print suites
    testSuite = unittest.TestSuite(suites)
    
    return testSuite
  #  print logger.info(test_file_strings)
if __name__ == '__main__':    
    if finddevices() == 'yes': # 检查是否已连接上手机
#        cleanEnv() #让导入find模块时就让执行了此步操作
        start_Appium('localhost','4723','4780','rst/appium.log')# 启动APPIUP服务 
        #logger加到此处eclispe才有日志输出
        #logger = log.Logger('rst/log.log',clevel = logging.DEBUG,Flevel = logging.INFO)
        timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        filename ='result_'+ timestr + '.html'
        print filename
        fp =open(filename,'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告',description=u'报告明细')
        runner.run(load_tests())
        #下面这句是原始的，不知道是什么意思，经过上面的改造，目前可以正常使用，且有报HTML报告输出
    #    unittest.TextTestRunner(verbosity=2).run(load_tests()) #
        fp.close()
        logging.shutdown()
        # 结束APPIUM服务
        stop_Appium('http://localhost:4723/wd/hub')