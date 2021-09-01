# @Author  : kane.zhu
# @Time    : 2021/7/20 18:03
# @Software: PyCharm
from pydantic import BaseModel

# 基于BaseModel 定义请求体的结构（json对象）
# 加密数据模型
class Plaintext(BaseModel):
    plaintext: str #默认是required


class Ciphertext(BaseModel):
    ciphertext: str


class Addconf(BaseModel):
    name: str
    conf_key: str
    conf_value: str
    category: str
    description : str = '' # 默认值为空 属于可选项