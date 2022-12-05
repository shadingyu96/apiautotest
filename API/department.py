import requests

from API.base_api import BaseApi
from API.wework import WeWork


class Department(BaseApi):
    list_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"

    def list(self, id):
        self.json_data = requests.get(self.list_url,
                                      params={"access_token": WeWork.get_token(),
                                              "id": id}).json()
        return self.json_data

