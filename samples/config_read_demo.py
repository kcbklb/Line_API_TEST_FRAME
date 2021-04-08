import configparser # 1.导入内置包
import os

config_file_path = os.path.join(os.path.dirname(__file__),'..','conf','config.ini')

cfg_obj = configparser.ConfigParser() # 2.创建一个配置文件对象
cfg_obj.read(config_file_path,encoding='utf-8') # 3.配置文件对象加载配置文件
# value = cfg_obj.get('default','HOSTS') # 4.使用get方法进行取值
value = cfg_obj.get('path','CASE_PATH')
print(value)

# 进行二次封装变成更适应框架的代码