'''
Created on 2016-5-21

@author: Administrator
'''
#_*_coding:utf-8_*_
import os
localpath = os.getcwd()
def getDeviceDetail():
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