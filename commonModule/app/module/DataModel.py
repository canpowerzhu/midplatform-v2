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
    module_name: str  # 模块名称 比如billing,cmdb等
    excel_data: dict
