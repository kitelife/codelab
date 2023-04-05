#该程序的版本1中，邮件的接收方，不能成功解析出邮件的主题Subject，
#这个版本使用MIMEText()来生成发送的内容

#在浏览网页的时候，我喜欢把我认为好的文章的链接发送到邮箱，作为收藏，
#但是每次都要打开邮件客户端或者浏览器，很麻烦，所以就写了这个命令行的
#邮件发送工具

import smtplib
import sys
from email.mime.text import MIMEText

mail_server = 'smtp.sjtu.edu.cn'
mail_server_port = 25
password = 'xxxxxx'

from_addr = 'youngsterxyf@sjtu.edu.cn'
to_addr=['sas.198708@gmail.com','youngsterxyf@sjtu.edu.cn']

msg = MIMEText(sys.argv[1])
msg['Subject'] = sys.argv[2]
msg['From'] = from_addr
msg['To'] = ";".join(to_addr)

s = smtplib.SMTP(mail_server,mail_server_port)
s.set_debuglevel(1)

s.login(from_addr,password)
s.sendmail(from_addr, to_addr, msg.as_string())
s.quit()
