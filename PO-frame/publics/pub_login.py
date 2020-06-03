
class login:
    def __init__(self,driver,user_name,password,login_button,keep_login=None,forget_pass=None,share_link=None):
        self.driver = driver
        self.user_name = user_name
        self.password = password
        self.keep_login = keep_login
        self.forget_pass = forget_pass
        self.share_link = share_link
        self.login_button = login_button

    def username_input(self,user_name):
        self.driver.find_element_by_name('login_info').send_keys(user_name)

    def pass_input(self,password):
        self.driver.find_element_by_name('password').send_keys(password)

    def keep_login(self,is_selected):
        if is_selected == False:
            self.driver.find_element_by_name('remember').click()

    def forget_pass(self):
        self.driver.find_element_by_class_name('getpassowrd_link').click()

    def share_link(self):
        self.driver.find_element_by_css_selector("a[href='/simple/oauth_login/id/5']").click()

    def login_button_click(self):
        self.driver.find_element_by_class_name('input_submit').click()

    def name_or_pass_wrong_alert(self):
        return self.driver.find_element_by_class_name('prompt').text


