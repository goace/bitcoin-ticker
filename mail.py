# -*- coding: utf-8 -*-  
import smtplib
import email.MIMEMultipart
import email.MIMEText
import email.MIMEBase
import os.path

class Mail:
    def __init__(self, my_name, smtp_addr, username, password):
        self.my_name = my_name
        self.smtp_addr = smtp_addr
        self.username = username
        self.password = password

    def send(self, to, subject, content):
        # login to the smtp server
        self.server = smtplib.SMTP(self.smtp_addr)
        self.server.login(self.username, self.password)
        
        # 构造MIMEMultipart对象做为根容器
        main_msg = email.MIMEMultipart.MIMEMultipart()
        
        # 构造MIMEText对象做为邮件显示内容并附加到根容器
        text_msg = email.MIMEText.MIMEText(content)
        main_msg.attach(text_msg)
        
        # 设置根容器属性
        main_msg['From'] = self.my_name
        main_msg['To'] = to
        main_msg['Subject'] = subject
        main_msg['Date'] = email.Utils.formatdate( )
        
        # 得到格式化后的完整文本
        full_text = main_msg.as_string( )
        
        #注意, 这里的第二个参数是个list, 否则如果给多人发邮件, 只有第一个人可以收到
        self.server.sendmail(self.my_name, to.split(','), full_text)

