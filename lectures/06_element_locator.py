# 1. 导包
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 2. 获取浏览器对象
driver = webdriver.Chrome()

# 3. 启动浏览器
driver.get("https://www.baidu.com/")

# 4. 最大化浏览器窗口
driver.maximize_window()

# 元素定位
# 一次定位一个元素
# ID: 属性定位
# driver.find_element(By.ID, 'kw').send_keys("刘亦菲")

# NAME: 属性名字定位
# driver.find_element(By.NAME, 'wd').send_keys("liuyifei")

# CLASS_NAME: 类名定位
# driver.find_element(By.CLASS_NAME, 'class_name').send_keys("刘亦菲")

# TAG_NAME: 标签定位
# selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable
# 由于页面中有多个input标签，selenium不知道操作哪一个
# 通过标签去定位元素的方法比较少用，因为一个页面中有很多相同标签，无法定位指定标签进行操作
# driver.find_element(By.TAG_NAME, 'input').send_keys("刘亦菲")

# # LINK_TEXT = "link test". 完整匹配
# driver.find_element(By.LINK_TEXT, "link_text")
#
# # PARTIAL_LINK_TEXT = "partial link text". 模糊匹配
# driver.find_element(By.PARTIAL_LINK_TEXT, "hao").click()

# time.sleep(5)

# driver.find_element(By.CSS_SELECTOR, '.s_ipt').send_keys("胡歌") # 通过 .类名 去定位
# driver.find_element(By.CSS_SELECTOR, '#kw').send_keys("胡歌") # 通过 #ID 去定位

# XPATH定位
driver.find_element(By.XPATH, "//*[@id='chat-textarea']").send_keys("彭于晏")
time.sleep(1)

# 一次定位多个元素，返回值是一个列表
# 注意：浏览器页面中加载元素和使用自动化代码去找元素的时候，页面结构会发生变化
# el_list = driver.find_elements(By.TAG_NAME, 'input')
# print(el_list)
# # 让页面暂停运行：使用python中的input函数，让程序挂起
# input()
# el_list[0]


# 5. 关闭浏览器
# 注意：代码执行完成之后，浏览器也会自动关闭，可以不需要手动关闭
# driver.close()
driver.quit()