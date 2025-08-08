# 1. 导包
import time

from selenium import webdriver

# 2. 获取浏览器对象
driver = webdriver.Chrome()

# 3. 启动浏览器 (页面跳转)
driver.get("https://www.google.ca/")
time.sleep(1)

# 导航
driver.get("https://www.bing.com/")
time.sleep(1)

# 后退
driver.back()
time.sleep(1)

# 前进
driver.forward()
time.sleep(1)

# 刷新
driver.refresh()
time.sleep(1)

# 5. 关闭浏览器
# 注意：代码执行完成之后，浏览器也会自动关闭，可以不需要手动关闭
# driver.close()
driver.quit()