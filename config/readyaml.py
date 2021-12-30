# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: readyaml.py   读取yaml文件
@time: 2021/12/24 17:14
"""

import yaml
def read_yaml(filename):
    with open(filename,encoding='utf8')as f:
        yaml_ = yaml.safe_load(f)
        return yaml_
