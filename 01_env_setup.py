# 1. 导包
import time

from selenium import webdriver

# 2. 获取浏览器对象
driver = webdriver.Chrome()

# 3. 启动浏览器
driver.get("https://www.google.ca/")

# 4. 强制等待5秒
time.sleep(5)

# 5. 关闭浏览器
# 注意：代码执行完成之后，浏览器也会自动关闭，可以不需要手动关闭
driver.close()