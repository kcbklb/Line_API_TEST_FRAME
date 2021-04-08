# re.sub函数
# 用于替换字符串中的匹配项
# re.sub(pattern,repl,string,count=0,flags=0)
# pattern 正则中的模式字符串
# repl 替换的字符串，也可为一个函数
# string 要被查找替换的原始字符串
# count 模式匹配后替换的最大次数，默认0表示替换所有的匹配

import re
# 13577668899 , 湖南号码
str1 = '135 7766 8899 , 湖南号码'
result_01 = str1.replace(' ','')
print(result_01)

str1 = '135 7766 8899 , 湖南号码' # 一个空格
result_02 = re.sub('\d\s+\d','',str1) # 1376899 , 湖南号码
print(result_02)
# result_03 = re.sub('(\d+) (\d+) (\d+)',r'\1\2\3',str1) # \1\2\3 表示()的分组
# result_03 = re.sub('(\d+) (\d+) (\d+)',r'\1\3\2',str1) # 13588997766 , 湖南号码
result_03 = re.sub('(\d+) (\d+) (\d+)',r'133',str1) # 133 , 湖南号码
print(result_03)

str2 = '135  7766 8899 , 湖南号码' # 多个空格
result_04 = re.sub('(\d+)\s+(\d+) (\d+)',r'\1\2\3',str2) # r 原字符集，不会被转码
print(result_04)

result_05 = re.sub('\s,.*$','',str2) # 135  7766 8899
print(result_05)



