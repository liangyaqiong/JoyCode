#注册封装
class regist:
    def __init__(self,driver,username_input,password_input,re_password_input,regist_button,vf_code_input=None):
        self.driver = driver
        self.username = username_input
        self.password = password_input
        self.re_password = re_password_input
        self.regist_button = regist_button
        self.vf_code_input = vf_code_input

    def input_username(self,username):
        self.driver.find_element_by_name('username').send_keys(username)

    def input_password(self,password):
        self.driver.find_element_by_name('password').send_keys(password)

    def re_input_password(self,re_password):
        self.driver.find_element_by_name('repassword').send_keys(re_password)

    def input_vf_code(self,vf_code):
        self.driver.find_element_by_name('captcha').send_keys(vf_code)

    def regist_button_click(self):
        self.driver.find_element_by_class_name('input_submit').click()
