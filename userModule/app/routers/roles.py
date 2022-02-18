# @Author  : kane.zhu
# @Time    : 2022/2/18 16:53
# @Software: PyCharm
from fastapi import  APIRouter

router = APIRouter(
    prefix='/roles',
    tags=["roles"],
    responses={404: {"description": "Not found"}},
)