import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.maximize_window()

# # 1. 定位到图片按钮
# image_btn = driver.find_element(By.XPATH, '//*[@id="right-tool"]/div[2]/div[3]/div/div')
# # 2. 点击图标 => 进入到选择本地文件的界面
# image_btn.send_keys("resources/liuyifei.jpg")

el = driver.find_element(By.ID, "chat-submit-button")
print(el.tag_name) # button
print(el.text) # 百度一下
print(el.get_attribute("type")) # submit
print(el.screenshot("screenshot.png")) # True

# 注意：代码执行完成之后，浏览器也会自动关闭，可以不需要手动关闭
driver.close()