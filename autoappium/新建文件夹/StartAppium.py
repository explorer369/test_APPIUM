#coding:utf-8
import os,sys,time
import subprocess
#os.chdir(sys.path[0])

def start_Appium(host, port, bootstrap_port, appium_log_path):
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
    
        
#start_Appium('127.0.0.1','4723','4780','appium.log')   
 
def cur_file_dir():
     #获取脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)
#打印结果
#getpath = cur_file_dir()

    
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





def start_Appium111(host, port, bootstrap_port, appium_log_path): #device_uid,
        #appium -p 4723 -bp 4724 -U 22238e79 --command-timeout 600
        errormsg = ""
        appium_server_url =""
        try:
            if  host:
                cmd ='start /b appium -a '+ host +' -p '+ str(port)+ ' --bootstrap-port '+ str(bootstrap_port) +  ' --session-override --log '+ '"'+appium_log_path + '" --command-timeout 600'  #' -U '+ device_uid+
                print cmd
               # p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #stdout=PIPE, stderr=PIPE)
                p = subprocess.call(cmd, shell=True,stdout=open('logs.log','w'),stderr=subprocess.STDOUT)
                print p
                appium_server_url = 'http://' + host +':' + str(port) +'/wd/hub'
                print appium_server_url
            else:
                print "port:%d is used!"%(port)
        except Exception, msg:
            errormsg = str(msg)
        return appium_server_url, errormsg
#print start_Appium111('127.0.0.1','4723','4780','appium.log')
