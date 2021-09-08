# @Author  : kane.zhu
# @Time    : 2021/7/9 18:17
# @Software: PyCharm

import time,hmac, hashlib,base64,urllib.parse,requests,json

class Webhook(object):
    """
    定义 钉钉webhook通知相关
    """
    def __init__(self,token,secret):
        """
        :param token: 需要发送给谁，以token来区别 保证其唯一值
        :param secret: 推送消息安全认证生成的签名 申请机器人会产生
        """
        self.token = token
        self.secret = secret

    def send(self,content):
        """
        :param content: 推送内容
        :return: bool 成功或者失败
        """
        timestamp = str(round(time.time() * 1000))
        secret_enc = self.secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format( timestamp, self.secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        #拿到签名sign
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

        #拼接请求地址
        api_url = "https://oapi.dingtalk.com/robot/send?access_token=" + self.token + "timestamp=" + timestamp  + "&sign=" + sign
        headers = {'Content-Type': 'application/json;charset=utf-8'}
        try:
            requests.post(url=api_url, data=json.dumps(content), headers=headers)
            return True
        except Exception as e:
            print(e)
            return False



    def record(self):
        pass
