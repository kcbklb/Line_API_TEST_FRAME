import smtplib
from email.mime.text import MIMEText

email_body = '''
<h1 align="center"> 接口自动化测试报告 </h1>
<p align="center"> 详情见附件 </p>
'''

email_obj = MIMEText(email_body,'html','utf-8')
email_obj['from'] = '291901652@qq.com' # 发件人
email_obj['to'] = '291901652@qq.com' # 收件人
email_obj['Cc'] =  '593218127@qq.com' # 抄送人
email_obj['subject'] = 'P5P6接口自动化测试报告'

smtp = smtplib.SMTP()
smtp.connect("smtp.qq.com")
# 邮箱授权码
smtp.login(user='291901652@qq.com',password='hsnhdiailrimcajh')
# smtp.sendmail('291901652@qq.com','291901652@qq.com',email_obj.as_string())
smtp.sendmail('291901652@qq.com',['291901652@qq.com','593218127@qq.com'],email_obj.as_string())
smtp.close()