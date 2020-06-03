#个人中心>我的优惠券

# 我的优惠券菜单
# 优惠券信息
# 积分兑换栏
# 立即兑换按钮

# 我的优惠券点击
# 积分兑换-立即兑换

class pub_my_discount():
    def __init__(self,driver,my_discount_menu,discount_detail,points_exchange_menu,exchange_button):

        self.driver = driver
        self.my_discount_menu = my_discount_menu
        self.discount_detail = discount_detail
        self.points_exchange_menu = points_exchange_menu
        self.exchange_button = exchange_button


    def my_discount_click(self):

        self.driver.find_element_by_xpath("//li/a[text()='我的优惠券']").click()

    def points_exchange(self):

        self.driver.find_element_by_css_selector("a.get-btn input:last-child").click()

