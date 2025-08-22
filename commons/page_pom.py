from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        # 定义两个实例属性:
        # 1. 驱动 driver
        # 2. 等待 wait
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # 自定义元素定位方法，继承原有的定位方法，优化添加显式等待
    def find_element(self, xpath: str):
        def f(d):
            return self.driver.find_element(By.XPATH, xpath)
        self.wait.until(f)
        return self.driver.find_element(By.XPATH, xpath)

    # 获取提示信息
    def get_message(self):
        # 使用匿名函数lambda: 显式等待元素出现
        self.wait.until(lambda d: d.find_element(By.XPATH, "//p[@class='prompt-msg']").text)
        msg = self.find_element("//p[@class='prompt-msg']").text
        return msg

    # 点击取消按钮
    def click_cancel_button(self):
        cancel_button = self.find_element("//span[text()='取消']")
        cancel_button.click()

    # 点击确定按钮
    def click_confirm_button(self):
        confirm_button = self.find_element("//span[text()='确定']")
        confirm_button.click()

    # 切换页面（iframe）
    def iframe(self):
        # 以开头是server ip地址的src来定位iframe
        form_frame = self.find_element('//iframe[starts-with(@src,"http://116.62.63.211/")]')
        self.driver.switch_to.frame(form_frame)