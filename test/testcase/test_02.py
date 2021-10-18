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
        MN_text = MN.text
        self.assertEqual("1111111", MN_text)

    def test_06(self):
        Atmospheric_ = Atmospheric_grid(self.driver)
        # GPS坐标获取
        Atmospheric_.click_GPS_got()
        GPS_longitude = Atmospheric_.find_element(Atmospheric_.longitude)
        GPS_longitude_text = GPS_longitude.text
        self.assertEqual("3011.424294,N", GPS_longitude_text)

    def test_07(self):
        Atmospheric_ = Atmospheric_grid(self.driver)
        # 仪器属性选择PM10
        Atmospheric_.click_instrument()
        instrument = Atmospheric_.find_element(Atmospheric_.instrument)
        instrument_text = instrument.text
        self.assertEqual("PM10", instrument_text)

    def test_08(self):
        Atmospheric_ = Atmospheric_grid(self.driver)
        # 浓度显示填写后设置
        Atmospheric_.send_key_concentration("15")
        Atmospheric_.click_concentration_set_up()
        concentration = Atmospheric_.find_element(Atmospheric_.concentration_display)
        concentration_text = concentration.text
        self.assertEqual("15", concentration_text)

    def test_09(self):
        Atmospheric_ = Atmospheric_grid(self.driver)
        # 滤膜长度
        Atmospheric_.click_Filter_membrane()
        Filter_membrane_text = Atmospheric_.find_element(Atmospheric_.Filter_membrane_text).text
        self.assertEqual("2950", Filter_membrane_text)


if __name__ == '__main__':
    pass
