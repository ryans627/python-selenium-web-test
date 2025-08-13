import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.maximize_window()

driver.find_element(By.XPATH, '//*[@id="chat-textarea"]').send_keys("美女")
driver.find_element(By.XPATH, '//*[@id="chat-submit-button"]').click()
# 1. 强制等待
# time.sleep(2)

# 2. 隐式等待
# driver.implicitly_wait(10) # 在10秒钟之内，不断地定位下面的元素，找到之后执行操作

# 3. 显式等待
# 需要把驱动传递过去，并且在10秒钟之内不断地定位该元素
# 如果出现了该元素，那么可以执行下面元素定位执行点击操作
# 如果在有效时间内，没有定位成功，那么程序会报错 TimeoutException: 等待超时
WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, '*[@id="chat-textarea1"]')))
driver.find_element(By.XPATH, '*[@id="chat-textarea"]')

# 注意：代码执行完成之后，浏览器也会自动关闭，可以不需要手动关闭
driver.close()
