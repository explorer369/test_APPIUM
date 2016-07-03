#coding:utf-8
import os,sys,time,re,subprocess
import log,logging
import unittest
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from  selenium.webdriver.support.ui import WebDriverWait
global driver,Testtime
localpath = os.getcwd()

#logger = log.Logger('rst/log.log',clevel = logging.DEBUG,Flevel = logging.INFO)
def finddevices():
    rst = os.popen('adb devices').readlines()
    devices = ''.join(rst)
    devices =  devices.count("device")
    if devices > 1:
        print ('共找到%s个手机'%(devices-1))
        return 'yes'
    else:
        print ('没有找到手机，请连接后再重试！')

def cleanEnv():
    '''每次执行命令时就把此rst目录删除,然后再新建rst,相当于清空上次的测试结果和日志
    '''                        
    os.system('adb kill-server')
    needClean = ['log.log','img','rst']   # 定义这=log.log,img,rst这三个值
    pwd = os.getcwd()                     # pwd=当前文件目录
    for i in needClean:                   # 循环needClean
        delpath = os.path.join(pwd,i)     # 结果为：当前目录\img和当前目录\rst  （例：C:\Users\Administrator\Desktop\测试结果\img）
        if os.path.isfile(delpath):
            cmd = 'del /f/s/q "%s"'% delpath   # 删除delpath得到的两个文件夹（img和rst）/F 强制删除只读文件/S 从所有子目录删除指定文件/Q 安静模式。删除全局通配符时，不要求确认。
            os.system(cmd)
        elif os.path.isdir(delpath):       # 否则，删除delpath得到的两个文件夹（img和rst）
            cmd = 'rd /s/q "%s"' %delpath
            os.system(cmd)
    if not os.path.isdir('rst/screenshot'):
     #   os.makedirs('rst')          
        os.makedirs('rst/screenshot/Failed')
        os.makedirs('rst/screenshot/Passed')
cleanEnv() #让导入此文件时就执行清除件和新建文件
logger = log.Logger('rst/log.log',clevel = logging.DEBUG,Flevel = logging.INFO)        
def find_name(self,method,TEXT,number=0):
        '''用法：self.find_name('id','com.wxws.myticket:id/rl_notification')
               self.find_name('name','点击')
               self.find_name('calss_name','android.widget.TextView')
               self.find_name('calss_names','android.widget.TextView',1)
               self.find_name('xpath',"//android.view.View[@index='2']")
        '''
        #此处logger和eclipse上输出日志有关联，加到这里会重复
        
        Testtime=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        if method == "name":
            try:
                emmm = self.driver.find_element_by_name(TEXT)
                #self.assertIsNotNone(emm)
                logger.info('+PASS+  Find the"%s"element'%TEXT)
                emmm.click()
                self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
                logger.info('+PASS+  Click on the "%s" element to succeed��Already screenshot'%TEXT)
            except NoSuchElementException, e:
              # print logger.info("Did not get to the control, click failed")
                self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
                print logger.info('+FAIL+  not found"%s"element ��Already screenshot'%TEXT)
              # return True   #�ӵ��˴�����ʾ�˲�ִ��ʧ�ܾͻ��˳��������������ʱ����ͰѴ˾�ע�ͼ��ɣ�
        if method == "id":
            try:
                emmm = self.driver.find_element_by_id(TEXT)
                #self.assertIsNotNone(emm)
                logger.info('+PASS+  Find the"%s"element'%TEXT)
                emmm.click()
                self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
                logger.info('+PASS+  Click on the "%s" element to succeed��Already screenshot'%TEXT)
            except NoSuchElementException, e:
                time.sleep(1)
              # print logger.info("Did not get to the control, click failed")
                self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
                print logger.info('+FAIL+  not found"%s"element ��Already screenshot'%TEXT)
              # return True
        if method == "xpath":
            try:
                emmm = self.driver.find_element_by_xpath(TEXT)
                #self.assertIsNotNone(emm)
                logger.info('+PASS+  Find the"%s"element'%TEXT)
                emmm.click()
                self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
                logger.info('+PASS+  Click on the "%s" element to succeed��Already screenshot'%TEXT)
            except NoSuchElementException, e:
                time.sleep(1)
              # print logger.info("Did not get to the control, click failed")
                self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
                print logger.info('+FAIL+  not found"%s"element ��Already screenshot'%TEXT)
              # return True
        if method == "calss_name":
            try:
                emmm = self.driver.find_element_by_calss_name(TEXT)
                #self.assertIsNotNone(emm)
                logger.info('+PASS+  Find the"%s"element'%TEXT)
                emmm.click()
                time.sleep(1)
                self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
                logger.info('+PASS+  Click on the "%s" element to succeed��Already screenshot'%TEXT)
            except NoSuchElementException, e:
                time.sleep(1)
              # print logger.info("Did not get to the control, click failed")
                self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
                print logger.info('+FAIL+  not found"%s"element ��Already screenshot'%TEXT)
              # return True
        if method == "calss_names":
            try:
                lis = self.driver.find_elements_by_class_name(TEXT)
                logger.info('+PASS+  Find the"%s"element'%TEXT)                            
                print lis[number].click()                  
                time.sleep(1)
                self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
                logger.info('+PASS+  Click on the "%s" element to succeed��Already screenshot'%TEXT)
            except NoSuchElementException, e:
                time.sleep(1)
              # print logger.info("Did not get to the control, click failed")
                self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
                print logger.info('+FAIL+  not found"%s"element ��Already screenshot'%TEXT)
              # return True
              
def getdevices():
    '''返回设备信息供需要时使用。devicename,andriodVersion,deviceModelName
    '''
    devicedetals = []
    #获取测试机SN名称
    deviceSN = os.popen('adb shell getprop ro.serialno'.format(localpath))
    '''下面加上去掉\r\n是为了去掉：如：deviceName":"8a8084a344417920308\r\n"
    '''
    devicename = deviceSN.readlines()[0].strip('\r\n')
#   devicename =  "'%s'"%eval('devicename') #转换为带引号的字符串 如：Android 转换为：'Android'
    devicedetals.append(devicename)
    #获取系安卓系统版本号
    version = os.popen('adb shell getprop ro.build.version.release'.format(localpath))
    andriodVersion = version.readlines()[0].strip('\r\n')
#   andriodVersion =  "'%s'"%eval('andriodVersion')#转换为带引号的字符串
    devicedetals.append(andriodVersion)
    #获取测试机机型设备名称
    deviceModel = os.popen('adb shell getprop ro.product.model'.format(localpath))
    deviceModelName = deviceModel.readlines()[0]
#   deviceModelName =  "'%s'"%eval('deviceModelName')#转换为带引号的字符串
    devicedetals.append(deviceModelName)
    
    '''
    #获取包名  (要使用此项请先把AAPT添加到环境变量)
    badging = os.popen('aapt dump badging C:\\Users\\Administrator\\Desktop\\12308.apk'.format(localpath))

#    badging 是一个对象，用readline()读取第一行用分隔提取 
#    获取的值如下：
#    package: name='com.wxws.myticket' versionCode='61' versionName='6.1.1'

    packagename = badging.readline().split("'")[1]
    devicedetals.append(packagename)
    '''
    
    return devicename,andriodVersion,deviceModelName  # 此处暂时不返回：packagename
    
    '''
    desired_caps = {
            'platformName': 'Android',
            'platformVersion': andriodVersion
            'deviceName': devicename
            'app': 'G:/app-wap-debug.apk',
            'app-package': packagename
            #下列暂未实现，不过当你没给这（包名，Activity）两个参数时，它会通过解析 apk 文件自动获取这两个参数。
           # 'app-activity':'.general.appmanage.AppStart' # package name 和 app-activity 的获取方法你可以看看 appium 的实现。当你没给这两个参数时，它会通过解析 apk 文件自动获取这两个参数。
     }
    '''

def start_Appium(host, port, bootstrap_port, appium_log_path):
    '''命令方法后台启动APPIUM
    用法：start_Appium('localhost','4723','4780','rst/appium.log')
    '''
    errormsg = ""
    appium_server_url =""
    cmd ='start /b appium -a '+ host +' -p '+ str(port)+ ' --bootstrap-port '+ str(bootstrap_port) +  ' --session-override --log '+ '"'+appium_log_path + '" --command-timeout 600'  #' -U '+ device_uid+
        #p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #stdout=PIPE, stderr=PIPE)
#    p = subprocess.call(cmd, shell=True,stdout=open('E:/logs.log','w'),stderr=subprocess.STDOUT)
    p = subprocess.call(cmd, shell=True,stdout=open('rst\cmdlogs.log','w'),stderr=subprocess.STDOUT)
    print p
    appium_server_url = 'http://' + host +':' + str(port) +'/wd/hub'
    time.sleep(5)
    print '启动APPIUM服务完成，访问的URL地址为：%s'%appium_server_url
def cur_file_dir():
#获取当前脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)
#打印结果
#getpath = cur_file_dir()
'''
# 调用BAT脚本方式结束APPIUM服务
def stop_Appium(Appium_url): 
 #   Appium_url = http://localhost:4723/wd/hub
    a = Appium_url.split(":")[2].split("/")[0]
    cmd = ('StopAppium.bat %s'%a)
 #   print cmd
    p = os.system(cmd)    #执行当前目录的BAT文件必须用system,用os.popen(cmd)就不行
    if p == 0:
        print '执行关闭APPIUM服务命令成功，状态：%s'%p
 #   print p.read()
#stop_Appium('http://127.0.0.1:4723/wd/hub')  # 调用方法
'''
def stop_Appium(Appium_url):
        #stop_Appium('http://127.0.0.1:4723/wd/hub')
        a = Appium_url.split(":")[2].split("/")[0]
        cmd = 'netstat -aon | findstr %s'%a
        p = os.popen(cmd).readlines()    #执行当前目录的BAT文件必须用system,用os.popen(cmd)就不行
        if p:  #判断列表不为空时
            p = ''.join(p).split('LISTENING')[1].split()[0].strip()#以LISTENING来判断真正的PID，避免TIME_WAIT或ESTABLISHED状态
            cmd = 'taskkill /f /pid %s'%p
            os.popen(cmd)
            print '执行关闭APPIUM服务命令成功，PID为：%s'%p
        else:
            print 'kill APPIUM服务失败，传入的端口号是 %s ，请检查是否开启或端口是否不一致！'%a  