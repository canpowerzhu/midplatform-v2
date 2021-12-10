# @Author  : kane.zhu
# @Time    : 2021/7/20 18:03
# @Software: PyCharm
from pydantic import BaseModel

class Plaintext(BaseModel):
    """
    基于BaseModel 定义请求体的结构（json对象）
    加密数据模型
    """
    plaintext: str  # 默认是required

class Ciphertext(BaseModel):
    """
    基于BaseModel 定义请求体的结构（json对象）
    解密数据模型
    """
    ciphertext: str

class Addconf(BaseModel):
    """
    新增配置项结构体
    """
    name: str
    conf_key: str
    conf_value: str
    category: str
    description: str = ''  # 默认值为空 属于可选项

class GetConfSearch(BaseModel):
    """
    用于相关配置的搜索
    """
    id: int
    conf_key:str = ''
    category: str

# upload pic request body
class OssPicReq(BaseModel):
    "上传base64图片"
    base64pic: str

class OssApkReq(BaseModel):
    file_stream: bytes

class OssExcelReq(BaseModel):
    app_name: str  # 模块名称 比如billing,cmdb等
    func_name: str
    excel_data: list


class OperateLog(BaseModel):
    """
    业务操作日志记录
    """
    traceId: str
    username: str
    protocol: str
    path: str
    ip: str
    params: str
    status: bool
    operate_type: int


class WebhookLog(BaseModel):
    """
    webhook 调用记录
    """
    name: str
    status: bool
    content: str


class LoginOut(BaseModel):
    """
    登陆与登出相关日志
    """
    traceId : str
    username: str
    status: bool
    ip: str
    os_type: str
    broswer_type: str
    broswer_version: str
    user_agent: str
    action: bool

class Webhook_Data(BaseModel):
    """
    dingTalk 发送数据结构体
    """
    token: str
    secret: str
    send_content: dict