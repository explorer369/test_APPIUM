#coding:utf-8
import os,sys,time,re,xlrd
import log,logging
import unittest
from find import *
#from selenium import webdriver
from appium import webdriver
#导入等待时间包
from  selenium.webdriver.support.ui import WebDriverWait
global driver,Testtime
optpath = os.getcwd()                      #获取当前操作目录（此文件夹所在目录）
imgpath = os.path.join(optpath,'img')      #截图目录（如：D:\Python27\img，也就是在当前目录生成一个IMG文件夹）
logger = log.Logger('rst\log.log',clevel = logging.DEBUG,Flevel = logging.INFO)
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
class AndroidTest(unittest.TestCase): 
    func = getattr(__import__('find'),'find_name')  #func()# 相当于执行find.py的foo函数   
    def setUp(self):     
  #     devicename,andriodVersion,deviceModelName,packagename = getdevices() #此处获取了包名，如想自动获取请在getDevices下设置要获取的APK路径
        devicename,andriodVersion,deviceModelName = getdevices()
        print '当前连接的机器SN为：%s 版本为：%s 型号为:%s'%(devicename,andriodVersion,deviceModelName)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = andriodVersion  # 连上手机自动获取
        desired_caps['deviceName'] = devicename           # 连上手机自动获取
        desired_caps['appPackage'] = 'com.wxws.myticket' # 此处手动填写，如想自动获取请在getDevices下设置要获取的APK路径和开启52行
        desired_caps['appActivity'] = 'com.myticket.activity.WelcomeActivity'
        desired_caps['unicodeKeyboard'] = True    #加上这两行可以输入中文了，输入的时候不会弹出输入法，有些元素不会被盖住
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()       
    def test12308click(self):                  
            time.sleep(4)
            listdata = excel_table_byindex('data.xlsx',0) # 路径不要用中文
            if(len(listdata) <= 0 ):
                assert 0,u"Excel数据库异常" 
            for i in range(0,int(len(listdata))):
                print 'Excel中共有：%s 行数据'%(len(listdata))
                time.sleep(6)
                self.func("id","com.wxws.myticket:id/etBecity")
                time.sleep(1)
                self.driver.find_element_by_id('com.wxws.myticket:id/etSearch').send_keys(listdata[i]['username'])
                self.func('calss_names','android.widget.TextView',1)
                time.sleep(1)
             #   self.func("id","com.wxws.myticket:id/tv_cancel")
                self.func("id","com.wxws.myticket:id/etEncity")
                self.driver.find_element_by_id('com.wxws.myticket:id/etSearch').send_keys(listdata[i]['password'])
                time.sleep(2)
                self.func('calss_names','android.widget.TextView',1)
                self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%(listdata[i]['username'])) #以输入的username来命名截图（注：如有不规则的字符时一定要注意）
                time.sleep(1)
               #self.func("calss_names","android.widget.TextView",7)
                self.func("id","com.wxws.myticket:id/btnQuery")
                time.sleep(2)
                self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\test.png")
            self.driver.close_app()
            


