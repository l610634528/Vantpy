#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json
from utils.config import Config


class get_login_token:
    c = Config()
    username = c.get('login').get('username')
    password = c.get('login').get('password')
    p = c.get('login').get('face_url')

    def login_token(self):
        postdata = {"UserName": self.username, "PassWd": self.password, "pattern": None}
        headers = {'content-type': 'application/json'}
        r = requests.post(self.p, data=json.dumps(postdata),
                          headers=headers)
        token_str = r.text
        token_dict = json.loads(token_str)
        if token_dict['stats'] == 'YES':
            return token_dict["access_token"]
        else:
            return False


if __name__ == '__main__':
    c = get_login_token()
    print(c.login_token())
