# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: base_config.py  #基础配置文件
@time: 2021/12/24 14:21
"""
import time

from selenium import webdriver


class Base_object:

    def __init__(self,driver):
        self.driver = driver


    def openbrowser(self,br='gc'):
        """
        打开浏览器
        :param br: gc=谷歌；ff=Firefox；ie=IE
       :return:
        """
        if br == 'gc':
            self.driver = webdriver.Chrome()
        elif br == 'ff':
            self.driver = webdriver.Firefox()
        elif br == 'ie':
            self.driver = webdriver.Ie()
        else:
            print('浏览器暂不支持！请在此添加实现代码')
        #默认隐式等待
        self.driver.maximize_window()


    def open(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def input_(self,loc,value):
        self.find_element(*loc).send_keys(value)

    def click(self,loc):
        self.find_element(*loc).click()

    def clear_all(self, loc):
        return self.driver.find_element(*loc).clear()

    def sleep(self,t=1):
        time.sleep(t)

    def quit(self):
        self.driver.quit()