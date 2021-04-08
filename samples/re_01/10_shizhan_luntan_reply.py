import requests
import random
import re

response = requests.get(url='http://47.107.178.45/phpwind/')
body_str = response.text
tids = re.findall('<a href="http://(.+?)/phpwind/read.php\?tid=(\d+)&fid=(\d+)" class="st" style="" title="(.+?)">(.+?)</a>',body_str)
tid_list = []
for tid in tids:
    tid_list.append(tid[1])
#     print(tid[1])

session = requests.session()

session.cookies.set("csrf_token","3ef9890d166b8a4a")
session.cookies.set("zFb_winduser","D3Ea7hbBNH97SkdPxXH2AQ2Ub8pN8EOg9%2FyY%2BpdThYUr5ZOOGiATm1bKNZg%3D")

post_data = {
    "csrf_token":"3ef9890d166b8a4a",
    "atc_content":"hello world%d"%random.randint(1000,5000),
    "tid":"%s"%tid_list[random.randint(0,19)]
}

session.post(url='http://47.107.178.45/phpwind/index.php?c=post&a=doreply&_getHtml=1',
             data=post_data)