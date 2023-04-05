import smtplib
import sys
from email.message import Message

mail_server = 'smtp.sjtu.edu.cn'
mail_server_port = 25
password='xxxxxx'
from_addr = 'youngsterxyf@sjtu.edu.cn'
to_addr=['sas.198708@gmail.com','youngsterxyf@sjtu.edu.cn']

from_header = 'From: %s\r\n' %from_addr
to_header = 'To: %s\r\n\r\n' %to_addr

subject_header = 'Subject: %s'%sys.argv[1]
print subject_header
body = sys.argv[2]
print body
email_message = '%s\n%s\n%s\n\n%s' %(from_header, to_header, subject_header, body)

print '*'*70

s = smtplib.SMTP(mail_server,mail_server_port)
s.set_debuglevel(1)

s.login(from_addr,password)
s.sendmail(from_addr,to_addr,email_message)
s.quit()
