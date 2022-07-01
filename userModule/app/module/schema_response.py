# @Author  : kane.zhu
# @Time    : 2022/2/22 11:38
# @Software: PyCharm
from pydantic import BaseModel


class Response(BaseModel):
    code: int
    msg: str
    data: list
