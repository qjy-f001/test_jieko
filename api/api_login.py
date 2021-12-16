import requests


class Apilogin:

    # 登录方法
    def api_post_login(self, url, headers):
        return requests.get(url, headers=headers)
