import smtplib
from email.mime.text import MIMEText
from email.header import Header
import json
from blogs.apps.apis.serializer import BlogCommentsSerializer, MessageSerializer
from blogs.apps.apis.models import Blog, Messages


def send_mail(instance):
    mail_host = ""  # 设置服务器 邮件发送服务器
    mail_user = ""  # 用户名 邮箱账号
    mail_pass = ""  # 口令 邮箱密码
    sender = '' # 发送人
    receivers = [instance['emails']]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    blog = Blog.objects.get(id=int(instance['blog_id']))
    title = None
    if blog:
        title = blog.title
    mail_message = """
    <p>您好:</p>
    <p>       我已经收到您在本博客www.oslozone.cn的评论<p>
    <p>       评论文章: %s</p>
    <p>       评论内容: %s</p>
    <p>       评论时间: %s</p>
    <p>       感谢您的评论/留言,我会尽快回复您</p>
    """ % (title, instance['content'], instance['create_time'])
    message = MIMEText(mail_message, 'html', 'utf-8')
    message['From'] = Header("OsloZone", 'utf-8')
    message['To'] = Header("OsloZone", 'utf-8')

    subject = '关于您在本博客评论的通知'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
    except smtplib.SMTPException:
        raise smtplib.SMTPException


def get_reply(func):
    def wrapper(request, *args, **kwargs):
        request_body = json.loads(request.body)
        comments_seri = BlogCommentsSerializer(data=request_body)
        if comments_seri.is_valid():
            send_mail(request_body)
        return func(request, *args, **kwargs)

    return wrapper


def reply_message_mail(instance):
    mail_host = ""  # 设置服务器 邮箱发送服务器
    mail_user = ""  # 邮箱用n户名
    mail_pass = ""  # 邮箱口令
    sender = '' # 发送者
    receivers = [instance['emails']]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    title = 'About.vue'
    mail_message = """
    <p>您好:</p>
    <p>       我已经收到您在本博客www.oslozone.cn的评论<p>
    <p>       评论文章: %s</p>
    <p>       评论内容: %s</p>
    <p>       评论时间: %s</p>
    <p>       感谢您的评论/留言,我会尽快回复您</p>
    """ % (title, instance['content'], instance['create_time'])
    message = MIMEText(mail_message, 'html', 'utf-8')
    message['From'] = Header("OsloZone", 'utf-8')
    message['To'] = Header("OsloZone", 'utf-8')

    subject = '关于您在本博客评论的通知'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
    except smtplib.SMTPException:
        raise smtplib.SMTPException


def reply_message(func):
    def wrapper(request, *args, **kwargs):
        request_body = json.loads(request.body)
        message_rerializer = MessageSerializer(data=request_body)
        if message_rerializer.is_valid():
            reply_message_mail(request_body)
            return func(request, *args, **kwargs)
        else:
            return

    return wrapper
