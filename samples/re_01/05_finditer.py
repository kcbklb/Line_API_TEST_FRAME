# re.finditer函数
# re.finditer和findall类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
# 语法：
# re.finditer(pattern,string,flags=0)

import re

# re.finditer 查找所有，并返回迭代器，迭代器中都是match对象
str1 = 'hello 123 hello'

pattern_01 = re.compile('\w+')
result_01 = pattern_01.finditer(str1,pos=5,endpos=12)
print(result_01)

for r in result_01:
    print(r.group())