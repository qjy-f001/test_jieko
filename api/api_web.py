import requests


class ApiWeb:

    # 登录方法
    def api_get_web(self, url, headers):
        return requests.get(url, headers=headers)
