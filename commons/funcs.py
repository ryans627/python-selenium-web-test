from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username, password):
    driver.get("http://116.62.63.211/shop/user/loginInfo.html")
    # 1. 输入账号
    driver.find_element(By.XPATH, "//input[@placeholder='请输入用户名/手机/邮箱']").send_keys(username)
    # 2. 输入密码
    driver.find_element(By.XPATH, "//input[@placeholder='请输入登录密码']").send_keys(password)
    # 3. 点击登录按钮
    driver.find_element(By.XPATH, "//button[text()='登录']").click()
    # 显式等待
    wait = WebDriverWait(driver, 10)
    # 可以继续优化代码，使用匿名函数lambda
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//p[@class='prompt-msg']"), "登录成功"))

    msg = driver.find_element(By.XPATH, "//p[@class='prompt-msg']").text
    return msg