import re

str1 = '''newdream come on!!
google come on!!'''

value = re.subn('(\w+) (\w+) (\w+)',r'\2 \3 \1',str1)
print(type(value))
print(value)

value = re.sub('(\w+) (\w+) (\w+)',r'\2 \3 \1',str1)
print(type(value))
print(value)