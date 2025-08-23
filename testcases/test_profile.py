import os.path
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from commons.funcs import login
from commons.login_page import LoginInfoPage
from commons.profile_page import SaveInfoPage, UserAvatarPage
from commons.user_address_page import UserAddressPage


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
        # 进入我的地址
        driver.get("http://116.62.63.211/shop/useraddress/index.html")
        # 点击新增地址按钮
        driver.find_element(By.XPATH, "//button[@data-popup-title='新增地址']").click()
        # 填写表单
        # 由于页面中有iframe标签元素，是属于页面中的子页面结构
        # 需要切换子页面之后再定位其中元素并操作
        # 定位iframe元素 => 注意：iframe的id是动态变化的. 不可信. 要手写xpath, 而不能直接copy
        # el = driver.find_element(By.XPATH, '//*[@id="am-modal-5wgn6"]/div/div[2]/iframe')
        # 直接使用src去定位
        el = driver.find_element(By.XPATH, "//iframe[@src='http://116.62.63.211/shop/useraddress/saveinfo.html']")
        # 切换子页面
        driver.switch_to.frame(el)
        # 输入姓名
        driver.find_element(By.XPATH, "//input[@placeholder='姓名']").send_keys("张三")
        # 输入电话
        driver.find_element(By.XPATH, "//input[@placeholder='电话']").send_keys("1111111111")
        # 从选择框中选择省市区
        # 选择省份
        # 点击省份标签元素
        driver.find_element(By.XPATH, "/html/body/div[1]/form/div[4]/div[1]/a/span").click()
        # 点击具体下拉框中的省份元素: 点击河北省
        driver.find_element(By.XPATH, "/html/body/div[1]/form/div[4]/div[1]/div/ul/li[4]").click()

        # 点击城市下拉框
        driver.find_element(By.XPATH, "/html/body/div[1]/form/div[4]/div[2]/a/span").click()
        # 选择城市：石家庄
        driver.find_element(By.XPATH, "/html/body/div[1]/form/div[4]/div[2]/div/ul/li[2]").click()

        # 点击区县下拉框
        driver.find_element(By.XPATH, "/html/body/div[1]/form/div[4]/div[3]/a/span").click()
        # 选择区: 井阱县
        driver.find_element(By.XPATH, "/html/body/div[1]/form/div[4]/div[3]/div/ul/li[2]").click()

        # 输入详细地址
        driver.find_element(By.XPATH, "//*[@id='form-address']").send_keys("第四胡同128号")

        # 点击保存按钮
        driver.find_element(By.XPATH, "//button[text()='保存']").click()

        # 断言：操作成功
        # 显式等待
        wait = WebDriverWait(driver, 10)
        # 使用匿名函数lambda
        wait.until(lambda d: driver.find_element(By.XPATH, "//p[@class='prompt-msg']"))

        msg = driver.find_element(By.XPATH, "//p[@class='prompt-msg']").text
        assert msg == "操作成功"
