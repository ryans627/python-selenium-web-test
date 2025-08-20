import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from commons.funcs import login


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

    msg = login(driver, 'ltqiu251', '123456')
    # 获取实际结果之后断言预期结果
    assert msg == "登录成功"
