# 导包
import unittest

import api
from api.api_login import Apilogin
from parameterized import parameterized

from tool.read_json import read_json


def get_data():
    arr = []
    arr.append(tuple(read_json("login.json").values()))
    return arr


# 新建测试类 继承
class TestLogin(unittest.TestCase):
    # 初始化方法
    def setUp(self):
        # 实例化ApiLogin对象
        self.login = Apilogin()

    # 测试方法
    @parameterized.expand(get_data())
    def test_login(self, url, headers):
        # 调用登录方法
        response = self.login.api_post_login(url,headers)
        # 断言 响应状态码
        self.assertEqual(response.status_code, 200)
        # 断言 响应信息
        # print(response.text)
        print(response.status_code)

        # self.assertEqual(expect, response.json().get("message"))

        # # 第一步 单独获取token
        # token = response.json().get("data").get("token")

        # # 第二步 将 token 添加到 headers字典中
        # api.headers['Authorization'] = "Bearer " + token

        # 一条语句 解决 token问题
        # case.headers['Authorization'] = "Bearer " +response.json().get("data").get("token")

        # print("动态设置的headers值为：", case.headers)
        # print("获取的token值为：", token)
        # print("响应结果：", response.json())
