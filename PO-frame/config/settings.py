import  os

# os.path.abspath(__file__)  #获取当前py文件的绝对路径
# os.path.dirname(os.path.abspath(__file__)) #获取当前py文件的目录路径
root_path =  os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #获取当前py文件的目录的上一层目录路径，在这里是项目的根目录的路径

driver_path = os.path.join(root_path,'webdriver')
screenshots_path = os.path.join(root_path,'screenshoots')
reports_path = os.path.join(root_path,'reports')
testcase_path = os.path.join(root_path,'case')
data_path = os.path.join(root_path,'data')
log_path = os.path.join(root_path,'logs')

