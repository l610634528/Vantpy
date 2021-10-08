#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from test.common.BrowserDriver import BrowserDriver


class model(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver = BrowserDriver(cls)
        cls.driver = driver.openbrowser(cls)

    def setUp(self):
        pass

    def teardown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
