from time import sleep
# from config import database
from selenium import webdriver
import unittest
from publics import pub_my_discount
from tools import tool_login

class my_discount(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://shop.aircheng.com/simple/reg')
        self.driver.maximize_window()
        self.discount = pub_my_discount.pub_my_discount(driver=self.driver,
                                   my_discount_menu = 'my_discount_menu',
                                   discount_detail = 'discount_detail',
                                   points_exchange_menu = 'points_exchange_menu',
                                   exchange_button = 'exchange_button')
        self.login = tool_login.tools(self.driver)
        self.login.login()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_my_discount_menu_skip(self):
        "菜单'我的优惠券'跳转"
        self.discount.my_discount_click()
        self.assertEqual('http://shop.aircheng.com/ucenter/redpacket',self.driver.current_url)

    def test_points_exchange(self):
        "积分不足，不能兑换"
        self.discount.my_discount_click()
        self.discount.points_exchange()
        self.assertEqual('积分不足，无法兑换',self.driver.find_element_by_css_selector("div.aui_content div").text)

if __name__ == '__main__':
        suite = unittest.TestSuite()
        # suite.addTest(my_discount('test_my_discount_menu_skip'))
        suite.addTest(my_discount('test_points_exchange'))

        runner = unittest.TextTestRunner()
        runner.run(suite)