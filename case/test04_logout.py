import unittest
import api
import case
from api.api_logout import ApiLogOut


class TestLogOut(unittest.TestCase):
    # 初始化
    def setUp(self):
        # 获取ApiChannels对象
        self.logout = ApiLogOut()

    # 测试方法
    def test_logout(self, url="http://127.0.0.1:8000/logout",
                    headers=case.headers):
        # 调用 获取所有频道
        # print(headers)
        response = self.logout.aip_get_logout(url, headers)
        print("响应结果：", response.status_code)
        # 断言 状态码：200
        self.assertEqual(200, response.status_code)
