# import unittest
# import api
# from api.api_logout import ApiLogOut
# # from case.test02_dologin import cookies
#
#
# class TestChannels(unittest.TestCase):
#     # 初始化
#     def setUp(self):
#         # 获取ApiChannels对象
#         self.logout = ApiLogOut()
#
#     # 测试方法
#     def test_get_channels(self, url="http://127.0.0.1:8000/logout"):
#         # 调用 获取所有频道
#         response = self.logout.aip_get_logout(url)
#         # 断言 状态码：200
#         self.assertEqual(200, response.status_code)
#         print("响应结果：", response.text)
