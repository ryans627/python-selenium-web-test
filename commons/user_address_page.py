# 定义用户地址页面类
from commons.base_page import BasePage


class UserAddressPage(BasePage):
    url = "http://116.62.63.211/shop/useraddress/index.html"
    user_name = "//span[@class='user']"
    phone = "//span[@class='phone']"
    address = "//span[@class='province']"

    # 定义实例方法
    def get_info(self):
        user_name_txt = self.find_element(self.user_name).text
        phone_txt = self.find_element(self.phone).text
        address_txt = self.find_element(self.address).text
        # 以tuple的形式返回
        return (user_name_txt, phone_txt, address_txt)
