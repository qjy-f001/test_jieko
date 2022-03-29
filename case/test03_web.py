import unittest
import api
import case
from api.api_web import ApiWeb


class TestWeb(unittest.TestCase):
    # 初始化
    def setUp(self):
        # 获取ApiChannels对象
        self.web = ApiWeb()

    # 测试方法
    def test_web(self, url='http://127.0.0.1:8000/web/#',
                 headers=case.headers):
        # 调用 获取所有频道
        response = self.web.api_get_web(url, headers)
        print(response.status_code)
        # print(response.text)

        self.assertEqual(response.status_code, 200)
