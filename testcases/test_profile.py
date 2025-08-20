import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from commons.funcs import login


@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.maximize_window()
    d.implicitly_wait(10)
    msg = login(d, 'beifan_1212', 'beifan_1212')
    assert msg == "登录成功"
    yield d
    d.quit()


# 由于个人中心用例脚本较多，使用类方式定义测试用例为实例方法
class TestProfile:
    # update and save user profile (info)
    def test_save_info(self, driver):
        driver.get("http://116.62.63.211/shop/user/index.html")
        # 点击"修改资料"按钮
        driver.find_element(By.XPATH, "//a[contains(text(),'修改资料')]").click()
        # 点击"编辑"按钮
        driver.find_element(By.XPATH, "//a[contains(text(),'编辑')]").click()
        # 保存昵称输入框元素
        nickname_input = driver.find_element(By.XPATH, "//input[@placeholder='昵称']")
        # 清空输入框的内容
        nickname_input.clear()
        # 输入新的内容
        nickname_input.send_keys("吴彦祖")
        # 选择性别
        driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/form/div[2]/div/label[3]/span").click()
        calendar = driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/form/div[3]/input")
        # 清空并选择生日日期
        calendar.clear()
        calendar.send_keys("2025-08-20")
        # 点击保存按钮
        driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/form/div[4]/button").click()
        # 显式等待
        wait = WebDriverWait(driver, 10)
        # 使用匿名函数lambda
        wait.until(lambda d: driver.find_element(By.XPATH, "//p[@class='prompt-msg']"))

        msg = driver.find_element(By.XPATH, "//p[@class='prompt-msg']").text
        assert msg == "编辑成功"