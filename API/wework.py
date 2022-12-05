import requests as requests

from API.base_api import BaseApi


class WeWork(BaseApi):
    corpid = "wwf55a566b6d1c6bd3"
    contact_secret = "lsgkRCZorU9MLTU7h-f7s0NsC_AJYoc9z7jWzwW2JlQ"
    token = dict()
    token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"

    @classmethod
    def get_token(cls, secret=contact_secret):
        # 避免重复请求，提高速度
        if secret not in cls.token.keys():
            r = cls.get_access_token(secret)
            cls.token[secret] = r["access_token"]
        return cls.token[secret]

    @classmethod
    def get_access_token(cls, secret):
        r = requests.get(cls.token_url, params={"corpid": cls.corpid, "corpsecret": secret})
        return r.json()
