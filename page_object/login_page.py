# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: login_page.py  登录的基本操作
@time: 2021/12/24 17:30
"""
from time import sleep

import allure
from selenium.webdriver.common.by import By

from base.base_config import Base_object


class Login_page(Base_object):
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'
    username = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/div[1]/input')
    password = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/div[2]/input')
    click_ = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')
    search_text = (By.XPATH,'//*[@id="search-input"]')
    search_click = (By.XPATH,'//*[@id="ai-topsearch"]')


    def login_test1(self,username,password):
        with allure.step('打开浏览器'):
            self.open()
        with allure.step('填写用户名'):
            self.input_(self.username,username)
        with allure.step('填写密码'):
            self.input_(self.password,password)
        with allure.step('点击登录'):
            self.click(self.click_)
        self.sleep(3)

    def login_test2(self,text):
        # with allure.step('打开浏览器'):
        #     self.open()
        with allure.step('填写内容进行搜索'):
            self.input_(self.search_text,text)
        # with allure.step('填写密码'):
        #     self.input_(self.password,)
        with allure.step('点击查询'):
            self.click(self.search_click)
        self.sleep(3)

