# import unittest
#
# import pytest
# import requests
#
#
# class TestLogin(unittest.TestCase):
#     def test_demo_01(self):
#         url = "http://127.0.0.1:8000/dologin"
#         date = {
#             "shop_id": "1",
#             "username": "zhangsan",
#             "pass": "123"
#         }
#         json = {
#             "shop_id": "1",
#             "username": "zhangsan",
#             "pass": "123"
#         }
#         # headers = {"Content-Type": "text/html; charset=utf-8"}
#         print(date)
#         # requese = requests.post(url=url, json=json)
#         requese = requests.post(url=url, data=date)
#         print(requese.text)
#
#
# if __name__ == '__main__':
#     pytest.main()
