from selenium.webdriver.common.by import By
from test.common.Seleniums import BasePage
from time import sleep


class Atmospheric_grid(BasePage):
    """
    在这里写定位器，通过元素属性定位元素对象
    """
    account = (By.XPATH, "//input[@placeholder='用户名']")
    password = (By.XPATH, "//input[@placeholder='密码']")
    button = (By.XPATH, "//span[@class='el-checkbox__inner']")
    login = (By.XPATH, "//button[@class='mgt']")
    # 环境监测
    environment_look = (By.XPATH, "//ul[@class='el-menu el-menu--horizontal el-menu--dark']/li[2]/div")
    # 数据查询
    match_cover = (By.XPATH, "//ul[@class='el-menu el-menu--horizontal el-menu--dark']/li[2]/ul/li[2]")
    # 设备运维
    Equipment = (By.XPATH, "//ul[@class='el-menu el-menu--horizontal el-menu--dark']/li[5]/div")
    # 远程控制
    long_range = (By.XPATH, "//ul[@class='el-menu el-menu--horizontal el-menu--dark']/li[5]/ul/div/li[2]/ul/li[5]")
    # CDMS-2000
    CDMS_2000 = (By.XPATH, "//div[@class='context']/div/div/label[5]")
    # 参数配置
    Parameter_configuration = (By.XPATH, "//div[@class='el-table__body-wrapper']/table/tbody/tr/td[12]/div/button[3]")
    # 设备信息-仪器IP信息-获取
    context_information = (By.XPATH, "//div[@class='context']/div/div/div/div/form/div[2]/div/button/span")
    IP_information = (By.XPATH, "//div[@class='context']/div/div/div/div/form/div/div/div")
    # 设备MN号-获取
    MN_number = (By.XPATH, "//div[@class='context']/div/div[2]/div/div/form/div[3]/div/button/span")
    MN_number_information = (By.XPATH, "//div[@class='context']/div/div[2]/div/div/form/div/div/div/input")
    # SIM卡
    SIM_number_get = (By.XPATH, "//div[@class='context']/div/div[2]/div[2]/div/form/div[3]/div/button/span")
    SIM_number = (By.XPATH, "//div[@class='context']/div/div[2]/div[2]/div/form/div/div/div/input")
    # 仪器GPS坐标
    GPS_longitude_got = (By.XPATH, "//div[@class='context']/div/div[3]/div/div/form/div[4]/div/button/span")
    longitude = (By.XPATH, "//div[@class='context']/div/div[3]/div/div/form/div/div/div/input")
    # 仪器属性
    instrument = (By.XPATH, "//div[@class='context']/div/div[3]/div[2]/div/form/div/div/div/input")
    PM10 = (By.XPATH, "//div[@x-placement='bottom-start']/div/div/ul/li")
    # 仪器属性点击
    def click_instrument(self):
        self.click(self.instrument)
        sleep(2)
        self.click(self.PM10)
        sleep(2)

    def input_Atmospheric_grid_account(self, text):
        self.send_key(self.account, text)

    def input_Atmospheric_grid_password(self, password):
        self.send_key(self.password, password)

    def click_remember_button(self):
        self.click(self.button)
        sleep(2)
        self.click(self.login)

    def click_match_cover(self):
        self.click(self.match_cover)
        sleep(2)

    def click_long_range(self):
        self.click(self.long_range)
        sleep(2)

    def click_CDMS_2000(self):
        self.click(self.CDMS_2000)
        sleep(3)
        self.click(self.Parameter_configuration)
        sleep(2)

    def click_get_information(self):
        self.click(self.context_information)
        sleep(2)

    # 获取设备MN号
    def click_MN(self):
        self.click(self.MN_number)
        sleep(2)

    # SIM卡获取
    def click_SIM(self):
        self.click(self.SIM_number_get)
        sleep(2)

    # GPS坐标获取
    def click_GPS_got(self):
        self.click(self.GPS_longitude_got)
        sleep(2)

