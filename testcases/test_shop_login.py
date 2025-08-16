import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# 前后置夹具
@pytest.fixture()
def driver():
    d = webdriver.Chrome()
    d.maximize_window()
    yield d
    d.quit()


def test_login(driver):
    # 1. 访问项目地址
    driver.get("http://116.62.63.211/shop/")
    # 2. 点击登录按钮
    driver.find_element(By.XPATH, "//a[text()='登录']").click()
    # 3. 断言：当前页面 == 登录页面
    # 修复bug: 得到的实际url有时包含大写字母，有时包含小写字母
    # expected_url和actual_url都集体小写
    actual_url = driver.current_url.lower()
    expected_url = "http://116.62.63.211/shop/user/loginInfo.html".lower()
    assert actual_url == expected_url
    # 4. 输入账号
    driver.find_element(By.XPATH, "//input[@placeholder='请输入用户名/手机/邮箱']").send_keys("ltqiu251")
    # 5. 输入密码
    driver.find_element(By.XPATH, "//input[@placeholder='请输入登录密码']").send_keys("123456")
    # 6. 点击登录按钮
    driver.find_element(By.XPATH, "//button[text()='登录']").click()

    # 由于代码执行速度过快，元素还未加载出来，所以定位不到 => 解决方法：使用等待让元素出现后再操作
    # 隐式等待
    # driver.implicitly_wait(10) # 使用隐式等待，在十秒钟之内不断地去定位实际结果元素

    # 显式等待
    # def func(d):
    #     """自定义显式等待函数必须满足以下要求:
    #         1. 必须接收参数: 一定要有一个形参
    #         2. 返回值必须为真（等待结束），返回值为假（继续等待）
    #     """
    #     driver.find_element(By.XPATH, "/html/body/div[10]/div/p")
    #     return True

    wait = WebDriverWait(driver, 10)

    # 可以继续优化代码，使用匿名函数lambda
    wait.until(lambda d: driver.find_element(By.XPATH, "//p[@class='prompt-msg']"))

    # 7. 断言: 系统提示信息（实际结果）== 登录成功（预期结果）
    msg = driver.find_element(By.XPATH, "//p[@class='prompt-msg']").text
    print(msg)
    # 获取实际结果之后断言预期结果
    assert msg == "登录成功"
