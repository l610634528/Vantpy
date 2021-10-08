#!/usr/bin/python3
# -*- coding: utf-8 -*-
# !/usr/bin/python3
# -*- coding: utf-8 -*-
from test.page.Atmospheric_Page import Atmospheric_grid
from test.testcase.case_modle import *
from common.elements import GetPageElements


class Atmospheric(model):
    element = GetPageElements('elements.yaml').login_page_elements()
    def gf(self):
        self.Atmospheric_ = Atmospheric_grid(self.driver)
        return self.Atmospheric_

    Atmospheric_ = gf()
    def test_Atmospheric(self):
        self.Atmospheric_.input_Atmospheric_grid_account(self.element['username'])
        self.Atmospheric_.input_Atmospheric_grid_password(self.element['password'])
        self.Atmospheric_.click_remember_button()
        self.assertIn('大气环境网格化综合监管平台', self.driver.title)

    def test_B(self):
        self.Atmospheric_.move_to_element(self.Atmospheric_.environment_look)


if __name__ == '__main__':
    pass
