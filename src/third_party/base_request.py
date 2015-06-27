from conf import SERVER_ADDR

import requests


class BaseRequest(object):

    def __init__(self, auth, url, payload):
        self.auth = auth
        self.url = SERVER_ADDR + url
        self.payload = payload

    def post(self):
        self.response = requests.post(self.url, auth=self.auth, json=self.payload)
