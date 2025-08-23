# 定义用户地址页面类
import time

from commons.base_page import BasePage


class UserAddressPage(BasePage):
    url = "http://116.62.63.211/shop/useraddress/index.html"
    user_name = "//span[@class='user']"
    phone = "//span[@class='phone']"
    address = "//span[@class='province']"

    # 定义实例方法
    def get_info(self):
        user_name_txt = self.find_element(self.user_name).text
        phone_txt = self.find_element(self.phone).text
        address_txt = self.find_element(self.address).text
        # 以tuple的形式返回
        return (user_name_txt, phone_txt, address_txt)

class SaveUserAddressPage(BasePage):
    url = "http://116.62.63.211/shop/useraddress/index.html"
    # 新增地址按钮
    add_btn = "//button[@data-popup-title='新增地址']"
    name_input = "//input[@placeholder='姓名']"
    phone_input = "//input[@placeholder='电话']"
    # province
    province_btn = "//span[text()='省份']"
    province_option = "/html/body/div[1]/form/div[4]/div[1]/div/ul/li[4]"
    # city
    city_btn = "//span[text()='城市']"
    city_option = "/html/body/div[1]/form/div[4]/div[2]/div/ul/li[2]"
    # county
    county_btn = "//span[text()='区/县']"
    county_option = "/html/body/div[1]/form/div[4]/div[3]/div/ul/li[2]"
    # detailed_address
    detailed_address_input = "//*[@id='form-address']"
    # save button
    save_btn = "//button[text()='保存']"

    def add_address(self, name, phone, detailed_address):
        self.find_element(self.add_btn).click()
        # 切换iframe的方法已经在BasePage中封装好了，直接调用即可
        self.iframe()
        self.find_element(self.name_input).send_keys(name)
        self.find_element(self.phone_input).send_keys(phone)

        self.find_element(self.province_btn).click()
        self.find_element(self.province_option).click()

        self.find_element(self.city_btn).click()
        self.find_element(self.city_option).click()

        self.find_element(self.county_btn).click()
        self.find_element(self.county_option).click()

        self.find_element(self.detailed_address_input).send_keys(detailed_address)
        self.find_element(self.save_btn).click()
        return self.get_message()
