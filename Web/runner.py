# coding:utf8


# @Time:    2021/12/27 22:56
# @Auth:    xiejun
# @filename:
import os

import pytest
# import allure_pytest

if __name__ == "__main__":
    pytest.main(['-s', '../test_suit/test_login.py', '--alluredir', '../result'])
    os.system('allure generate ../result/ -o ../report_allure/ --clean')
