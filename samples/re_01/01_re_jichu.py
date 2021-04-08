'''
1.常用元字符
.  匹配任意除换行符"\n"外的字符
+ 匹配前一个字符1次或无限次
.+匹配多个除换行符"\n"外的字符
？匹配一个字符0次或1次，还有一个功能是可以防止贪婪匹配
^ 匹配字符串开头
$  匹配字符串末尾
|   匹配该符号两边的一个
()  匹配括号内的表达式，也表示一个组
[]  匹配字符组中的字符
[^]匹配除了字符组中字符的所有字符
{n} 重复n次
{n,}重复n次或更多次
{n,m}重复n到m次

2.预定义字符集表
\d 匹配数字
\D 匹配非数字
\w 匹配字母或数字或下划线
\W 匹配非字母或数字或下划线
\s 匹配任意的空白符
\S 匹配非空白符
\n 匹配一个换行符
\t 匹配一个制表符
\A 仅匹配字符串开头，同^
\Z 仅匹配字符串结尾，同$
\b 匹配一个单词边界，也就是指单词和空格间的位置
'''
# 正则表达式基础
import re

str1 = 'newdream'
str2 = '''
hello123hello
hello123
hello12
12hello
hello12ho
''' # 以换行开头
# 方式一:
pattern_01 = re.compile('n\w+m')
result_01 = re.match(pattern_01,str1)
print(result_01.group())

pattern_02 = re.compile('hello\d+h')
result_02 = re.findall(pattern_02,str2)
print(result_02)

# 方式二:
result_03 = re.match('n\w+m',str1)
print(result_03.group())

# 方式三:
result_04 = pattern_01.match(str1)
print(result_04.group())