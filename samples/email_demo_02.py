import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_body = '''
<h1 align="center"> 接口自动化测试报告 </h1>
<p align="center"> 详情见附件 </p>
'''
html_file_path = os.path.join(os.path.dirname(__file__),'..','html_reports','WX_API_TEST_V1.7','WX_API_TEST_V1.7.html')

text_obj = MIMEText(email_body,'html','utf-8')

attach_file = MIMEText(open(html_file_path,'rb').read(),'base64','utf-8')
attach_file['Content-type'] = 'application/octet-stream'
# attach_file.add_header('Content-Disposition','attachment',filename=('gbk','','WX_API_TEST_V1.7.html'))
attach_file['Content-Disposition']='attachment;filename="WX_API_TEST_V1.7.html"'

email_obj = MIMEMultipart()
email_obj.attach(text_obj)
email_obj.attach(attach_file)
email_obj['from'] = '291901652@qq.com' # 发件人
email_obj['to'] = '291901652@qq.com' # 收件人
email_obj['Cc'] =  '593218127@qq.com' # 抄送人
email_obj['subject'] = 'P5P6接口自动化测试报告'

smtp = smtplib.SMTP()
smtp.connect("smtp.qq.com")
# 邮箱授权码
smtp.login(user='291901652@qq.com',password='hsnhdiailrimcajh')
smtp.sendmail('291901652@qq.com','291901652@qq.com',email_obj.as_string())
# smtp.sendmail('291901652@qq.com',['291901652@qq.com','593218127@qq.com'],email_obj.as_string())
smtp.close()