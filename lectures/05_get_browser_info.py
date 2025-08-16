# 1. 导包
from selenium import webdriver

# 2. 获取浏览器对象
driver = webdriver.Chrome()

# 3. 启动浏览器
driver.get("https://www.google.ca/")

# 4. 获取浏览器信息
print(f"获取浏览器标题：{driver.title}")
print(f"获取浏览器网址：{driver.current_url}")
# print(f"获取浏览器HTML：{driver.page_source}")
# print(f"获取浏览器截图：{driver.get_screenshot_as_file("page.png")}")
print(f"获取元素对象：{driver.find_element("xpath", "//a")}")

# 5. 关闭浏览器
# 注意：代码执行完成之后，浏览器也会自动关闭，可以不需要手动关闭
# driver.close()
driver.quit()