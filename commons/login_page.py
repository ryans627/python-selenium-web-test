# 定义一个登录页面类
#  - 整个类代表整个页面
#    - 类中的属性，代表页面中的元素
#    - 类中的方法，代表页面中的操作
import logging

from commons.base_page import BasePage
logger = logging.getLogger('pom')

# 继承BasePage
class LoginInfoPage(BasePage):
    # 将页面中的元素，定义成类属性
    # 登录页面地址
    url = "http://116.62.63.211/shop/user/loginInfo.html"
    # 账号输入框
    username_input = "//input[@placeholder='请输入用户名/手机/邮箱']"
    # 密码输入框
    password_input = "//input[@placeholder='请输入登录密码']"
    # 确认按钮
    submit_button = "//button[text()='登录']"

    # 将用例执行步骤封装成实例方法
    def login(self, username, password):
        self.find_element(self.username_input).send_keys(username)
        self.find_element(self.password_input).send_keys(password)
        self.find_element(self.submit_button).click()
        logger.info("登录成功")
        # 返回实际结果
        return self.get_message()