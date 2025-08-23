import os.path
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from commons.funcs import login
from commons.login_page import LoginInfoPage
from commons.profile_page import SaveInfoPage, UserAvatarPage
from commons.user_address_page import UserAddressPage, SaveUserAddressPage


@pytest.fixture(scope='class')
# 设置fixture为class级别
# 类中所有的实例方法（用例）全部可以获取已登录状态fixture
# 然后再执行脚本
# 不需要每个用例调用一次登录
def driver():
    d = webdriver.Chrome()
    d.maximize_window()
    # 发送请求访问项目地址 => 通过LoginInfoPage的类属性url访问
    d.get(LoginInfoPage.url)
    # 创建页面对象
    login_page = LoginInfoPage(d)
    msg = login_page.login('salewond', '123456')
    assert msg == "登录成功"
    yield d
    d.quit()


# 由于个人中心用例脚本较多，使用类方式定义测试用例为实例方法
class TestProfile:
    # update and save user profile (info)
    def test_save_info(self, driver):
        driver.get(SaveInfoPage.url)
        save_info_page = SaveInfoPage(driver)
        msg = save_info_page.submit("张三", "2025-04-01")
        assert msg == "编辑成功"

    def test_user_avatar(self, driver):
        driver.get(UserAvatarPage.url)
        user_avatar_page = UserAvatarPage(driver)
        msg = user_avatar_page.update_avatar(
            "/Users/ryanshang/Dev/mashang/python_selenium_web_tests/resources/liuyifei.jpg")
        assert msg == "上传成功"

    def test_address(self, driver):
        driver.get(UserAddressPage.url)
        user_address_page = UserAddressPage(driver)
        info = user_address_page.get_info()
        assert info == ("张三", "1111111111", "河北省")

    def test_save_user_address(self, driver):
        driver.get(SaveUserAddressPage.url)
        save_user_address_page = SaveUserAddressPage(driver)
        msg = save_user_address_page.add_address("张三", "1111111111","第四胡同128号")
        assert msg == "操作成功"