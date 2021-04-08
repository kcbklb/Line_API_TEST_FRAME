# re.match尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就会返回none
# 函数语法
# re.match(pattern,string,flags=0)
# pattern 匹配的正则表达式
# string 要匹配的字符串
# flags 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等

import re

str1 = 'hello123hello'  # 3hello123hello 3hello
# result = re.match('\d+hello',str1) # match匹配开头


str2 = '''hello123hello
hello1hello
''' # 以换行开头
# result = re.match('hello[\d,\D]+o',str2)

str3 = '''
hello123hello
hello1hello
'''
result_01 = re.match('\shello[\d\D]+o',str3)
print(result_01.group())

str4 = 'newdream come on!'

# result_02 = re.match('.+ .+ .+',str4) # 空格 普通字符
# result_02 = re.match('.+',str4)
result_02 = re.match('(.+) (.+) (.+)',str4)
print(result_02.group(3))
print(result_02.group(2))
print(result_02.group(1,3))
print(result_02.group())

str5 = 'newdream come on!'

result_03 = re.match('(.+) COme (.+)!',str5,re.I) # 标志位 re.I 忽略大小写 re.M 多行模式
print(result_03.group())

# group(num)或group()匹配对象函数来获取匹配表达式
# group(num=0)匹配的整个表达式的字符串，group()可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组
