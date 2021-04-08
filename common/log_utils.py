import os
import logging
import time

current_path = os.path.dirname(__file__)
log_output_path = os.path.join(current_path,'..','logs') # 日志输出路径

class LogUtils:
    def __init__(self,log_path=log_output_path):
        self.log_file_path = os.path.join(log_path,'api_test_log_%s.log'%time.strftime('%Y%m%d')) # %s格式控制字符串 日志文件具体路径
        self.logger = logging.getLogger('WX_api_test_log')
        self.logger.setLevel(logging.DEBUG) # 10

        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(self.log_file_path,'a',encoding='utf-8')
        formatter = logging.Formatter("%(asctime)s__%(name)s__%(levelname)s__%(message)s")
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

        console_handler.close() # 防止日志打印重复
        file_handler.close() # 防止日志打印重复

    def get_logger(self):
        return self.logger
# 建议日志用一个对象去输出
logger = LogUtils().get_logger()

if __name__ =='__main__':
    logger.info('执行接口测试用例开始...')
    # LogUtils().logger.info('执行接口测试用例开始') # 日志打印重复
    logger.info('执行接口测试用例开始')