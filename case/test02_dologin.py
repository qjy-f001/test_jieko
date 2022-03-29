# 导包
import unittest

import api
import case
from api.api_dologin import ApiDologin
from parameterized import parameterized

from tool.read_json import read_json


def get_data():
    arr = []
    arr.append(tuple(read_json("dologin.json").values()))
    return arr


# 新建测试类 继承
class TestDoLogin(unittest.TestCase):
    # 初始化方法
    def setUp(self):
        # 实例化ApiLogin对象
        self.dologin = ApiDologin()

    # 测试方法
    @parameterized.expand(get_data())
    def test_dologin(self, url, data, expect):
        # 调用登录方法
        response = self.dologin.api_post_dologin(url, data)
        # print(url, data)
        # print(response.headers)
        # 断言 响应状态码
        self.assertEqual(response.status_code, expect)
        # 断言 响应信息
        print(response.status_code)
        # print(response.cookies.get("sessionid"))

        # self.assertEqual(expect, response.json().get("sessionid"))

        # # 第一步 单独获取token
        # token = response.cookies.get("sessionid")
        #
        # # 第二步 将 token 添加到 headers字典中
        # api.headers['Cookie'] = "sessionid=" + token

        # 一条语句 解决 token问题
        case.headers['Cookie'] = "sessionid=" + response.cookies.get("sessionid")

        # print("动态设置的headers值为：", case.headers)
        # # print("获取的token值为：", token)
        # print("响应结果：", case.headers['Cookie'])
