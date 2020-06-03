from time import sleep
# from config import database
from selenium import webdriver
import unittest
from publics import pub_regist
from tools import log_output
class regist_case(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://shop.aircheng.com/simple/reg')
        self.driver.maximize_window()
        self.regist = pub_regist.regist(driver=self.driver,
                                   username_input = 'username_input',
                                   password_input = 'password_input',
                                   re_password_input = 're_password_input',
                                   regist_button = 'regist_button'
        )
        # self.data_base = database.database()
        self.log = log_output.log_output()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_username_short(self):
        "用户名长度少于2位"

        self.regist.input_username('1')
        self.regist.input_password('123456')
        self.regist.regist_button_click()
        sleep(2)
        self.assertIn('invalid-text',self.driver.find_element_by_name('username').get_attribute('class'))
        self.log.log_print(filename='case_regist', log_info='用例用户名长度校验执行成功！')


    def test_vf_code_wrong(self):
        "验证码错误"
        self.regist.input_username('liangyaqiong')
        self.regist.input_password('123456')
        self.regist.re_input_password('123456')
        self.regist.input_vf_code('DDDDD')
        self.regist.regist_button_click()
        self.assertIn('图形验证码输入不正确',self.driver.find_element_by_css_selector("div.aui_content div").text)


    @unittest.skip('数据库不能访问时忽略')
    def test_regist_success(self):
        self.regist.input_username('liangyaqiong')
        self.regist.input_password('123456')
        self.regist.re_input_password('123456')
        sleep(10)
        self.regist.regist_button_click()
        #断言校验数据库数据
        self.assertEqual('liangyaqiong',self.data_base.select_sql_excute(
                         sql = "select username from user_info where user_name='liangyaqiong';"),
                         query_key = 'username')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(regist_case('test_username_short'))
    suite.addTest(regist_case('test_vf_code_wrong'))
    suite.addTest(regist_case('test_regist_success'))

    runner = unittest.TextTestRunner()
    runner.run(suite)