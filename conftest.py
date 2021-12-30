# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: conftest.py
@time: 2021/12/30 14:58
"""

# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: conftest.py
@time: 2021/12/30 14:13
"""
import allure
import pytest
from selenium import webdriver

driver = None

@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item, call):
    #什么时候去识别用例的执行结果
    #后置处理
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        #在这里实现失败截图和添加allure附件
        img = driver.get_screenshot_as_png()
        #截图方法需要用到driver对象
        allure.attach(img,'运行结果截图',allure.attachment_type.PNG)


@pytest.fixture(scope='session',autouse=True)
def init_driver():
    global driver
    driver = webdriver.Chrome()
    return driver
