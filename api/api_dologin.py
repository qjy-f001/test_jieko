import requests


class ApiDologin:

    # 登录方法
    def api_post_dologin(self, url, data):
        return requests.post(url, data=data)
