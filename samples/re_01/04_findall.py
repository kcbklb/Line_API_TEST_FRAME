# re.findall函数 查找所有
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
# findall(string[,pos[,endpos]])
# string:待匹配的字符串
# pos:可选参数，指定字符串的起始位置，默认为0
# endpos:可选参数，指定字符串的结束位置，默认为字符串的长度

import re

str1 = 'hello 123 hello'
result_01 = re.search('\w+',str1)
result_02 = re.findall('\w+',str1)
result_03 = re.findall('\w+d',str1)

pattern_01 = re.compile('\w+')
result_04 = pattern_01.findall(str1,pos=5,endpos=12)

print(result_01) # 返回obj
print(result_02) # 返回列表
print(result_03) # 找不到不会报错，返回空列表
print(result_04)