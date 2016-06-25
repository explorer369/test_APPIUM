#coding:utf-8
import os,sys,time,re,xlrd
import log,logging
import unittest
#from selenium import webdriver
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
#导入等待时间包
from  selenium.webdriver.support.ui import WebDriverWait
global driver,Testtime
optpath = os.getcwd()                      #获取当前操作目录（此文件夹所在目录）
imgpath = os.path.join(optpath,'img')      #截图目录（如：D:\Python27\img，也就是在当前目录生成一个IMG文件夹）
logger = log.Logger('rst/log.log',clevel = logging.DEBUG,Flevel = logging.INFO)
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
def open_excel(file= 'file.xls'):
  try:
    data = xlrd.open_workbook(file)
    return data
  except Exception,e:
    print str(e)
#根据索引获取Excel表格中的数据  参数:file：Excel文件路径   colnameindex：表头列名所在行的所以 ，by_index：表的索引
def excel_table_byindex(file= 'file.xls',colnameindex=0,by_index=0):
  data = open_excel(file)
  table = data.sheets()[by_index]
  nrows = table.nrows #行数
  ncols = table.ncols #列数
  colnames = table.row_values(colnameindex) #某一行数据
  list =[]
  for rownum in range(1,nrows):
    row = table.row_values(rownum)
    if row:
      app = {}
      for i in range(len(colnames)):
        app[colnames[i]] = row[i]
      list.append(app)
  return list
class test_001_cls(unittest.TestCase):
    str1 = 'find'
    str2 = 'find_name'
    module = __import__(str1)  #导入demo
    #在demo模块里获取str2即foo函数并赋给func
    func = getattr(module,str2)
    #func()# 相当于执行demo模块下的foo函数 
    def setUp(self):
      desired_caps = {}
      desired_caps['automationName'] = 'appium'
      desired_caps['platformName'] = 'Android'
      desired_caps['platformVersion'] = '4.1'
      desired_caps['deviceName'] = '2596baed'
      desired_caps['appPackage'] = 'com.wxws.myticket'
      desired_caps['appActivity'] = 'com.myticket.activity.WelcomeActivity'
      desired_caps['unicodeKeyboard'] = True    #加上这两行可以输入中文了，输入的时候不会弹出输入法，有些元素不会被盖住
      desired_caps['resetKeyboard'] = True
      self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()
               
    def test_yy_click(self):
        time.sleep(10)
        self.func('id','com.wxws.myticket:id/rl_notification') #进入活动
        '''
        self.driver.find_element_by_id('com.wxws.myticket:id/etBecity').send_keys(u'深圳')
        time.sleep(2)
        self.driver.find_element_by_id('com.wxws.myticket:id/etEncity').send_keys(u'广州')
        time.sleep(2)
        self.func("id","com.wxws.myticket:id/btnQuery")
        '''
        time.sleep(2)
        self.func('xpath',"//android.widget.LinearLayout[@index='0']") #进入第一个活动
        time.sleep(2)
        # 用于返回被测app是NATIVE_APP还是WEBVIEW，如果两者都有就是混合型App
        print self.driver.contexts #输出到屏幕
        time.sleep(5)
        #切换到WEBVIES(如果点击不到的话就把此切换WEB关闭)
        #self.driver.switch_to.context(u'WEBVIEW_com.wxws.myticket') 
        time.sleep(8)
        #点击WEBview里的控件
        self.func('xpath',"//android.view.View[@index='2']")
        time.sleep(5)
       
    
            


