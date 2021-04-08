# re.search函数 全字符查找 找到第一个就停止
# 扫描整个字符串并返回第一个成功的匹配
# re.search(pattern,string,flags=0)
# 匹配成功re.search方法返回一个匹配的对象，否则返回None
# 不是从开头找，任意的只要满足都行
import re

str1 = 'nEwDreamEaaaa'
# pattern_01 = re.compile('E\w')
# pattern_01 = re.compile('e\w',re.IGNORECASE)
# result_01 = re.search(pattern_01,str1)
result_01 = re.search('e\w',str1,re.I)
print(result_01.group())