# @Author  : kane.zhu
# @Time    : 2021/7/20 18:03
# @Software: PyCharm
from pydantic import BaseModel

# 基于BaseModel 定义请求提的结构（json对象）
# 加密数据模型
class Plaintext(BaseModel):
    plaintext: str #默认是required
    testmsg: str = False #可选项


class Ciphertext(BaseModel):
    ciphertext: str

