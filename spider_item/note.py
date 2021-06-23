# 导入第三方模块
import smtplib
import time
from configparser import ConfigParser
from email.mime.text import MIMEText
from email.utils import formataddr

# 自定义发送邮件的函数
'''	
    配置发邮件所需的基础信息	
    my_sender    # 配置发件人邮箱地址	
    my_pass      # 配置发件人邮箱密码	
    to_user      # 配置收件人邮箱地址	
    my_nick      # 配置发件人昵称	
    to_nick      # 配置收件人昵称	
    mail_msg     # 配置邮件内容	
'''


def mail(my_sender, my_pass, to_user, my_nick, to_nick, mail_msg):
    # 必须将邮件内容做一次MIME的转换 -- 这是发送含链接的邮件
    msg = MIMEText(mail_msg, 'html', 'utf-8')
    # 配置发件人名称和邮箱地址
    msg['From'] = formataddr([my_nick, my_sender])
    # 配置收件件人名称和邮箱地址
    msg['To'] = formataddr([to_nick, to_user])
    # 配置邮件主题（标题）
    msg['Subject'] = "提示"
    # 配置Python与邮件的SMTP服务器的连接通道（如果不是QQ邮箱，SMTP服务器是需要修改的）
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    # 模拟登陆
    server.login(my_sender, my_pass)
    # 邮件内容的发送
    server.sendmail(my_sender, [to_user, ], msg.as_string())
    # 关闭连接通道


def load_config():
    cfg = ConfigParser()
    cfg.read('.\\config.ini', encoding='utf-8')
    return cfg.get('email', 'my_sender'), cfg.get('email', 'my_pass'), cfg.get(
        'email', 'to_yser'), cfg.get('email', 'my_nick'), cfg.get('email', 'to_nick')


def run_note(s):
    c = load_config()
    mail(c[0], c[1], c[2], c[3], c[4], s)


def log(s):
    f = open('.\\log.txt', 'a', encoding='utf-8')
    f.write(s)
    f.close()


def log_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
