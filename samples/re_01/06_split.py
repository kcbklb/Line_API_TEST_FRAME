# re.split方法按照能够匹配的子串将字符串分割后返回列表
# 函数语法：
# re.split(pattern,string,maxsplit=0,flags=0)
# pattern 匹配的正则表达式
# string 要匹配的字符串
# maxsplit 分割次数，maxsplit=1 分隔一次，默认为0，不限制次数
# flags 标志位，用于控制正则表达式的匹配方式 如：是否区分大小写，多行匹配等等

import re

str1 = '中国$韩国$泰国$英国'
print(str1.split('$'))

str2 = '中国1韩国2泰国3英国'
# print(str2.split('1'))
print(re.split('\d',str2))
print(re.split('\d',str2,maxsplit=2)) # maxsplit=1 分隔一次，默认为0，不限制次数

str3 = '中国 韩国  泰国     英国   德国'
print(re.split('\s+',str3))