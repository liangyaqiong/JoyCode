
class tools:

    def __init__(self,driver):

        self.driver = driver
    def login(self):

        self.driver.find_element_by_link_text('登录').click()
        self.driver.find_element_by_css_selector("input[name='login_info']").send_keys('liangyq')
        self.driver.find_element_by_css_selector("input[name='password']").send_keys('123456')
        self.driver.find_element_by_css_selector('.input_submit').click()
