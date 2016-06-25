#coding:utf-8
import os,sys,time,re
import log,logging
import unittest
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from  selenium.webdriver.support.ui import WebDriverWait
global driver,Testtime
logger = log.Logger('rst/log.log',clevel = logging.DEBUG,Flevel = logging.INFO)
def find_name(self,method,TEXT,number=0):

        Testtime=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        if method == "name":
            try:
                emmm = self.driver.find_element_by_name(TEXT)
                #self.assertIsNotNone(emm)
                print logger.info('+PASS+  Find the"%s"element'%TEXT)
                emmm.click()
                self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
                print logger.info('+PASS+  Click on the "%s" element to succeed��Already screenshot'%TEXT)
            except NoSuchElementException, e:
              # print logger.info("Did not get to the control, click failed")
                self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
                print logger.info('+FAIL+  not found"%s"element ��Already screenshot'%TEXT)
              # return True   #�ӵ��˴�����ʾ�˲�ִ��ʧ�ܾͻ��˳��������������ʱ����ͰѴ˾�ע�ͼ��ɣ�
        if method == "id":
            try:
                emmm = self.driver.find_element_by_id(TEXT)
                #self.assertIsNotNone(emm)
                print logger.info('+PASS+  Find the"%s"element'%TEXT)
                emmm.click()
                self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
                print logger.info('+PASS+  Click on the "%s" element to succeed��Already screenshot'%TEXT)
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
                print logger.info('+PASS+  Find the"%s"element'%TEXT)
                emmm.click()
                self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
                print logger.info('+PASS+  Click on the "%s" element to succeed��Already screenshot'%TEXT)
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
                print logger.info('+PASS+  Find the"%s"element'%TEXT)
                emmm.click()
                time.sleep(1)
                self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
                print logger.info('+PASS+  Click on the "%s" element to succeed��Already screenshot'%TEXT)
            except NoSuchElementException, e:
                time.sleep(1)
              # print logger.info("Did not get to the control, click failed")
                self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
                print logger.info('+FAIL+  not found"%s"element ��Already screenshot'%TEXT)
              # return True
        if method == "calss_names":
            try:
                lis = self.driver.find_elements_by_class_name(TEXT)
                print logger.info('+PASS+  Find the"%s"element'%TEXT)                            
                print lis[number].click()                  
                time.sleep(1)
                self.driver.get_screenshot_as_file("rst\\screenshot\\Passed\\%s.png"%Testtime)
                print logger.info('+PASS+  Click on the "%s" element to succeed��Already screenshot'%TEXT)
            except NoSuchElementException, e:
                time.sleep(1)
              # print logger.info("Did not get to the control, click failed")
                self.driver.get_screenshot_as_file("rst\\screenshot\\Failed\\%s.png"%Testtime)
                print logger.info('+FAIL+  not found"%s"element ��Already screenshot'%TEXT)
              # return True
