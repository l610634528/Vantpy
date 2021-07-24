#!/usr/bin/python3
# -*- coding: utf-8 -*-
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Email   : 944921374@qq.com

import unittest
import sys

from test.page.Atmospheric_grid import Atmospheric_grid
from test.testcase.case_modle import *
from common.elements import GetPageElements

class Atmospheric(model):
    element = GetPageElements('elements.yaml').login_page_elements()
    def test_Atmospheric(self):
        Atmospheric_ = Atmospheric_grid(self.driver)
        Atmospheric_.input_Atmospheric_grid_account(self.element['username'])
        Atmospheric_.input_Atmospheric_grid_password(self.element['password'])
        Atmospheric_.click_remember_button()
        # baidu.get_screent_img("baidu")
        self.assertIn('大气环境网格化综合监管平台', self.driver.title)
        # self.assertIn("sss",self.driver.title)


if __name__ == '__main__':
    pass
