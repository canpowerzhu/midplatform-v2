# @Author  : kane.zhu
# @Time    : 2022/7/27 11:24
# @Software: PyCharm
# @Description:
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
from app.settings import PrdConfig


class EmailHook(object):
    # 定义 邮件webhook通知相关
    def __init__(self, receiver):
        """
        :param receiver:
        :param msg:
        :param subject:
        """

        self.receiver = receiver

    def send(self, subject, msg):
        """

        :param subject:
        :param msg:
        :return:
        """
        message = MIMEText(msg, 'html', 'utf-8')
        message['From'] = Header(PrdConfig.EMAIL_FROM_ACCOUNT,'utf-8')
        message ['To'] = Header(self.receiver)
        message['Subject'] = Header(subject, 'utf-8')

        try:
            mailobj = SMTP_SSL(PrdConfig.EMAIL_HOST)

            mailobj.login(PrdConfig.EMAIL_FROM_ACCOUNT, PrdConfig.EMAIL_FROM_ACCOUNT_PASS)
            mailobj.sendmail(PrdConfig.EMAIL_FROM_ACCOUNT, self.receiver, message.as_string())
            flag = True
        except smtplib.SMTPException:
            flag = False
        return flag

    # 发送成功与否记录日志，供来查看
    def record(self):
        pass
