from Tools.utils import Utils


class BaseApi:
    json_data = None

    def jsonpath(self, expr):
        return Utils.jsonpath(self.json_data, expr)
