import logging

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger('pom')

class BasePage:
    def __init__(self, driver):
        logger.info(f'Initiating the Page Object: {self.__class__.__name__}')
        # 定义两个实例属性:
        # 1. 驱动 driver
        # 2. 等待 wait
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # 自定义元素定位方法，继承原有的定位方法，优化添加显式等待
    def find_element(self, xpath: str):
        logger.info(f'Locating the element with xpath: {xpath}')
        def f(d):
            return self.driver.find_element(By.XPATH, xpath)
        self.wait.until(f)
        logger.info(f'Located the element: {xpath}')
        return self.driver.find_element(By.XPATH, xpath)

    # 获取提示信息
    def get_message(self):
        logger.info("Getting the system notification message...")
        # 使用匿名函数lambda: 显式等待元素出现
        self.wait.until(lambda d: d.find_element(By.XPATH, "//p[@class='prompt-msg']").text)
        msg = self.find_element("//p[@class='prompt-msg']").text
        logger.info(f'System notification message: {msg}')
        # 保存截图
        png = self.driver.get_screenshot_as_png()
        allure.attach(png, '系统提示信息')
        return msg

    # 点击取消按钮
    def click_cancel_button(self):
        cancel_button = self.find_element("//span[text()='取消']")
        cancel_button.click()
        logger.info("Cancel button was clicked.")

    # 点击确定按钮
    def click_confirm_button(self):
        confirm_button = self.find_element("//span[text()='确定']")
        confirm_button.click()
        logger.info("Confirm button was clicked.")

    # 切换页面（iframe）
    def iframe(self):
        logger.info("Ready to switch iframe.")
        # 以开头是server ip地址的src来定位iframe
        form_frame = self.find_element('//iframe[starts-with(@src,"http://116.62.63.211/")]')
        logger.info(f"iframe was successfully switched to: {form_frame}")
        self.driver.switch_to.frame(form_frame)
