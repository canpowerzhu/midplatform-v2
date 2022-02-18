# @Author  : kane.zhu
# @Time    : 2022/2/18 16:52
# @Software: PyCharm

from fastapi import  APIRouter

router = APIRouter(
    prefix='/users',
    tags=["users"],
    responses={404: {"description": "Not found"}},
)
