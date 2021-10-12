#!/usr/bin/python3
# -*- coding: utf-8 -*-
# !/usr/bin/python3
# -*- coding: utf-8 -*-
from test.page.Atmospheric_Page import Atmospheric_grid
from test.testcase.case_modle import *
from common.elements import GetPageElements
from time import sleep


class Atmospheric(model):
    element = GetPageElements('elements.yaml').login_page_elements()

    def test_01(self):
        Atmospheric_ = Atmospheric_grid(self.driver)
        Atmospheric_.input_Atmospheric_grid_account(self.element['username'])
        Atmospheric_.input_Atmospheric_grid_password(self.element['password'])
        Atmospheric_.click_remember_button()
        # baidu.get_screent_img("baidu")
        self.assertIn('大气环境网格化综合监管平台', self.driver.title)
        # self.assertIn("sss",self.driver.title)

    def test_02(self):
        Atmospheric_ = Atmospheric_grid(self.driver)
        Atmospheric_.move_to_element(Atmospheric_.environment_look)
        Atmospheric_.click_match_cover()

    def test_03(self):
        Atmospheric_ = Atmospheric_grid(self.driver)
        Atmospheric_.move_to_element(Atmospheric_.Equipment)
        Atmospheric_.click_long_range()

    def test_04(self):
        Atmospheric_ = Atmospheric_grid(self.driver)
        # 进入CDMS-2000参数配置,点击获取
        Atmospheric_.click_CDMS_2000()
        IP = Atmospheric_.find_element(Atmospheric_.IP_information)
        IP_text = IP.text
        self.assertEqual("11.70.11.1", IP_text)

    def test_05(self):
        Atmospheric_ = Atmospheric_grid(self.driver)
        # 设备MN号获取信息
        Atmospheric_.click_MN()
        MN = Atmospheric_.find_element(Atmospheric_.MN_number_information)
        MN_title = MN.text
        self.assertEqual("1111111", MN)

    def test_06(self):
        Atmospheric_ = Atmospheric_grid(self.driver)



if __name__ == '__main__':
    pass
