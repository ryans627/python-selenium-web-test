# 定义用户地址页面类
import logging
import time

from selenium.webdriver.common.by import By

from commons.base_page import BasePage
logger = logging.getLogger('pom')

class UserAddressPage(BasePage):
    url = "http://116.62.63.211/shop/useraddress/index.html"
    user_name = "//span[@class='user']"
    phone = "//span[@class='phone']"
    address = "//span[@class='province']"

    # 定义实例方法
    def get_info(self):
        logger.info("正在获取信息")
        user_name_txt = self.find_element(self.user_name).text
        phone_txt = self.find_element(self.phone).text
        address_txt = self.find_element(self.address).text
        logger.info(f"获取到的信息内容为: {user_name_txt}, {phone_txt}, {address_txt}")
        # 以tuple的形式返回
        return user_name_txt, phone_txt, address_txt


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
        logger.info("Selecting province...")
        self.find_element(self.province_btn).click()
        self.find_element(self.province_option).click()
        logger.info("Selecting city...")
        self.find_element(self.city_btn).click()
        self.find_element(self.city_option).click()
        logger.info("Selecting county...")
        self.find_element(self.county_btn).click()
        self.find_element(self.county_option).click()
        logger.info("Inputing detailed address...")
        self.find_element(self.detailed_address_input).send_keys(detailed_address)
        self.find_element(self.save_btn).click()
        return self.get_message()

class DeleteAddressPage(BasePage):
    url = "http://116.62.63.211/shop/useraddress/index.html"
    # 注意：因为有多个地址，即多个删除按钮，通过以下这个xpath会得到多个搜索结果
    delete_btn_xpath = "//a[contains(text(), '删除')]"

    def delete_address(self, num: int):
        """
        :param num: starts from 0
        :return:
        """
        delete_btn_list = self.driver.find_elements(By.XPATH, self.delete_btn_xpath) # 返回一个列表
        delete_btn = delete_btn_list[num]
        logger.info(f"Clicking delete button on index: {num}")
        delete_btn.click()
        self.click_confirm_button()
        logger.info("Getting delete info...")
        return self.get_message()