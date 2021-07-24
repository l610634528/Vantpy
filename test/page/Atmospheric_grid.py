from selenium.webdriver.common.by import By
from test.common.Seleniums import BasePage


class Atmospheric_grid(BasePage):
    """
    在这里写定位器，通过元素属性定位元素对象
    """
    account = (By.XPATH, "//input[@placeholder='用户名']")
    password = (By.XPATH, "//input[@placeholder='密码']")
    button = (By.XPATH, "//span[@class='el-checkbox__inner']")
    login = (By.XPATH, "//button[@class='mgt']")
    def input_Atmospheric_grid_account(self, text):
        self.send_key(self.account, text)

    def input_Atmospheric_grid_password(self, password):
        self.send_key(self.password, password)

    def click_remember_button(self):
        self.click(self.button)
        self.click(self.login)