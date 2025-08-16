import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


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
    driver.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div[2]/a[1]").click()
    # 3. 断言：当前页面 == 登录页面
    url = driver.current_url
    assert url == "http://116.62.63.211/shop/user/loginInfo.html"
    # 4. 输入账号
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input").send_keys("ltqiu251")
    # 5. 输入密码
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input").send_keys("123456")
    # 6. 点击登录按钮
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button").click()

    # 由于代码执行速度过快，元素还未加载出来，所以定位不到 => 解决方法：使用等待让元素出现后再操作
    driver.implicitly_wait(10) # 使用隐式等待，在十秒钟之内不断地去定位实际结果元素
    # 7. 断言: 系统提示信息（实际结果）== 登录成功（预期结果）
    msg = driver.find_element(By.XPATH, "/html/body/div[10]/div/p").text
    print(msg)
    # 获取实际结果之后断言预期结果
    assert msg == "登录成功"