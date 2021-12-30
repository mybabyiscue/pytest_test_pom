# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: test_login.py
@time: 2021/12/24 14:27
"""
from time import sleep

import allure
import pytest
from selenium import webdriver

from base.base_config import Base_object
from config.readyaml import read_yaml
from page_object.login_page import Login_page

@allure.feature('电商项目Web自动化测试') #allure的title
class Test_login:

    @allure.title('打开浏览器')
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.lp = Login_page(cls.driver)
        # cls.web = Base_object()
        # cls.driver1 = cls.web.openbrowser()
        # cls.lp = Login_page(cls.driver1)

    @classmethod
    def teardown_class(cls):
        # cls.web = Base_object()
        cls.driver.quit()

    @allure.story('登录')
    @pytest.mark.parametrize('loginlist',read_yaml('../data/login.yaml'))
    def test_1login(self,loginlist):
        allure.dynamic.title(loginlist['title'])
        allure.description(loginlist['description'])
        self.lp.login_test1(loginlist['username'],loginlist['password'])

    @allure.story('查询')
    def test_2search(self):
        allure.dynamic.title("正确查询")
        allure.description("这是一个正确的查询")
        try:
            self.lp.login_test2('手机')
            assert 1==2
        except:
            pytest.fail('用例执行失败')
        finally:
            allure.attach(self.driver.get_screenshot_as_png(),'运行结果截图',allure.attachment_type.PNG)


if __name__ == '__main__':
    pytest.main('-sv')
