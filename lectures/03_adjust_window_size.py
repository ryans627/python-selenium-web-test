# 1. 导包
import time

from selenium import webdriver

# 2. 获取浏览器对象
driver = webdriver.Chrome()

# 3. 启动浏览器
driver.get("https://www.google.ca/")

# 4. 最大化
driver.maximize_window()
time.sleep(1)
# 5. 最小化
driver.minimize_window()
time.sleep(1)
# 6. 指定浏览器窗口分辨率
driver.set_window_size(300, 600)
time.sleep(1)

# 5. 关闭浏览器
# 注意：代码执行完成之后，浏览器也会自动关闭，可以不需要手动关闭
# driver.close()
driver.quit()