#!/usr/bin/python3
# -*- coding: utf-8 -*-
# !/usr/bin/python3
# -*- coding: utf-8 -*-
from test.page.Atmospheric_Page import Atmospheric_grid
from test.testcase.case_modle import *
from common.elements import GetPageElements


class Atmospheric(model):
    element = GetPageElements('elements.yaml').login_page_elements()

    def test_Atmospheric(self):
        Atmospheric_ = Atmospheric_grid(self.driver)
        Atmospheric_.input_Atmospheric_grid_account(self.element['username'])
        Atmospheric_.input_Atmospheric_grid_password(self.element['password'])
        Atmospheric_.click_remember_button()
        self.assertIn('大气环境网格化综合监管平台', self.driver.title)

    def test_B(self):
        Atmospheric_ = Atmospheric_grid(self.driver)
        Atmospheric_.move_to_element(Atmospheric_.environment_look)
        Atmospheric_.click_match_cover()


if __name__ == '__main__':
    pass
