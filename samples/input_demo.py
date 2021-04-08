import sys
value = sys.argv[1]
print('您输入的是：%s'%value)

# cmd从命令行读取参数
# D:\Line_API_TEST_FRAME\samples>python input_demo.py hello,world
# 您输入的是：hello,world
#
# D:\Line_API_TEST_FRAME\samples>python input_demo.py aaa
# 您输入的是：aaa

# import shutil
# shutil.copyfile('test.log','test1.log')
# copyfile 强制复制不提醒