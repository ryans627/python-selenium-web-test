import time

from commons.base_page import BasePage


class SaveInfoPage(BasePage):
    # 所有页面元素都定义为类属性
    # 个人中心页面地址
    url = "http://116.62.63.211/shop/user/index.html"
    # 修改资料按钮
    edit_profile_btn = "//a[contains(text(),'修改资料')]"
    # 编辑按钮
    edit_btn = "//a[contains(text(),'编辑')]"
    # 昵称输入框元素
    nickname_input = "//input[@placeholder='昵称']"
    # 性别单选框
    gender_radio = "/html/body/div[4]/div[3]/div/form/div[2]/div/label[3]/span"
    # 日期选择(日历)
    calendar_input = "//input[@placeholder='生日']"
    # 确认按钮
    save_btn = "//button[text()='保存']"

    # 将用例执行步骤封装成实例方法
    def submit(self, nickname: str, date: str):
        self.find_element(self.edit_profile_btn).click()
        self.find_element(self.edit_btn).click()
        # 名字输入框
        nickname_el = self.find_element(self.nickname_input)
        # 清空名字
        nickname_el.clear()
        time.sleep(5)
        # 输入名字
        nickname_el.send_keys(nickname)
        # 选择性别
        self.find_element(self.gender_radio).click()
        # 选择日期
        self.find_element(self.calendar_input).send_keys(date)
        # 点击确认按钮
        self.find_element(self.save_btn).click()
        # 返回实际结果
        return self.get_message()

class UserAvatarPage(BasePage):
    url = "http://116.62.63.211/shop/user/index.html"
    edit_avatar_btn = "//a[contains(text(),'修改头像')]"
    select_image_btn = "//input[@type='file']"
    upload_btn = "//button[text()='确认上传']"

    def update_avatar(self, path):
        self.find_element(self.edit_avatar_btn).click()
        self.find_element(self.select_image_btn).send_keys(path)
        time.sleep(1)
        self.find_element(self.upload_btn).click()
        return self.get_message()