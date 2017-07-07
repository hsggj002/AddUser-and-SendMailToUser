#-*- coding:utf-8 -*-
#Author: Guangjie Guo


import sys, os
from email.mime.text import MIMEText
import random
# base_dir = os.path.dirname(os. path.dirname(os.path.abspath(__file__)))
# sys.path.append(base_dir)

from email import encoders
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from db import db_file




def send_mail(name,password,mail):
    from_addr = 'xxx@163.com'  #输入发送邮件的账号
    password = 'xxx'   #输入发送邮件的密码
    to_addr = mail
    smtp_server = 'smtp.163.net'

    mail_msg = """
        用户名: %s
        密码: %s
    """%(name,password)

    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = Header(u'[重要]账号', 'utf-8').encode()

    msg.attach(MIMEText(mail_msg,'plain','utf-8'))

    with open('ReadME','rb') as f:
        mime = MIMEBase('txt', 'txt', filename='ReadME')
        mime.add_header('Content-Disposition', 'attachment', filename='ReadME')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        msg.attach(mime)


    server = smtplib.SMTP(smtp_server, 25)
    #server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


    print("用户创建成功，邮件已发送至用户邮箱...")


def init_sql():
    db_file.cre_sql()

    return read_file()

def read_file():
    with open('psw-file','r') as f:
        for i in f.readlines():
            l = i.split(' ')
            l[0], l[1] = l[0], l[1].replace('\n', '')
            db_file.ins_sql(l[0], l[1])


    print("数据库初始化成功")


def add_user(name,password,mail):
    with open('file-psd','r') as f:
        for i in f.readlines():
            if name in i:
                print("用户已存在，请重试")
                exit()

    db_file.ins_sql(name,password)
    v = db_file.sel_sql()

    with open('file-psd','w') as e:
        pass

    for i in v:
        with open('file-psd','a') as f:
            f.write("%s %s\n" % (i[1], i[2]))


    return send_mail(name,password,mail)


def del_user(name):
    with open('psw-file','a') as e:
        pass

    v = db_file.sel_sql()

    for i in v:
        if name == i[1]:
            db_file.del_sql(name)
            print("删除用户成功")
            break
    else:
        print("用户名不存在。。。")

    c = db_file.sel_sql()

    for i in c:
        with open('psw-file','a') as f:
            f.write("%s %s\n"%(i[1],i[2]))


