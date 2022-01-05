import requests


class ApiLogOut:
    # 获取用户下所有频道
    def aip_get_logout(self, url, headers):
        # 返回 响应对象
        return requests.get(url, headers=headers)
