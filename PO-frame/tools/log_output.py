# 导入logging模块
import logging
import time

from config import settings
#
#
#
class log_output:
    def __init__(self):
        pass

    def log_print(self,filename,log_info,log_error=None,log_warning=None,log_debug=None):
        # # 通过basicConfig()来设置日志的level
        # logging.basicConfig(level=logging.DEBUG,
        #                     filename=settings.log_path+filename+'.log',
        #                     filemode="w",
        #                     format="%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s:%(message)s")



            logger = logging.getLogger()
            logger.setLevel(logging.INFO)  # Log等级总开关
            # 创建一个handler，用于写入日志文件
            fh = logging.FileHandler(settings.log_path+'\\'+filename+'.log', mode='w')
            fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

            # 定义handler的输出格式
            formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
            fh.setFormatter(formatter)
            logger.addHandler(fh)
            logger.error(log_info, exc_info=True)
