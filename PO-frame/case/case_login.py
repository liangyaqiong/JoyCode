
from selenium import webdriver
import unittest
from publics import pub_login



class login_test(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://shop.aircheng.com/simple/login')
        self.login = pub_login.login(driver=self.driver,
                                user_name='account',
                                password='passord_input',
                                login_button='login_button_click'
        )


    def tearDown(self) -> None:
        self.driver.quit()

    def test_pass_wrong(self):
        "登录密码错误"
        self.login.username_input('123')
        self.login.pass_input('1256563')
        self.login.login_button_click()
        self.assertIn('账号或密码错误',self.login.name_or_pass_wrong_alert())

    def test_name_wrong(self):
        "登录名错误"
        self.login.username_input('liangya')
        self.login.pass_input('123456')
        self.login.login_button_click()
        self.assertIn('账号或密码错误',self.login.name_or_pass_wrong_alert())

    def test_login_sucess(self):
        "成功登录"
        self.login.username_input('liangyq')
        self.login.pass_input('123456')
        self.login.login_button_click()
        self.assertIn('liangyq，欢迎您', self.driver.find_element_by_css_selector("div[class='user_info'] h2").text)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(login_test('test_pass_wrong'))
    suite.addTest(login_test('test_name_wrong'))
    suite.addTest(login_test('test_login_sucess'))

    runner = unittest.TextTestRunner()
    runner.run(suite)