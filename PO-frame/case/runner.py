import  HTMLTestRunner
import  unittest
from config import settings
import time

from config.settings import testcase_path


def case_runner():
    suite = unittest.TestSuite()
    case_discover = unittest.defaultTestLoader.discover(testcase_path,pattern='case*.py',top_level_dir=None)
    for test_file in case_discover:
        for case in test_file:
           suite.addTests(case)
    return suite


cur_time = time.strftime("%Y年%m月%d日%H-%M-%S", time.localtime(time.time()))
report_name = settings.reports_path + '\\'+'report_'+cur_time+'.html'
exl = open(report_name,'w+',encoding='utf-8')
runner = HTMLTestRunner.HTMLTestRunner(stream=exl,title='登录注册个人中心测试报告',description='测试报告')
runner.run(case_runner())


