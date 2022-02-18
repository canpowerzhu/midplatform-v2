# @Author  : kane.zhu
# @Time    : 2022/2/18 16:53
# @Software: PyCharm
from fastapi import  APIRouter

router = APIRouter(
    prefix='/usergroups',
    tags=["usergroups"],
    responses={404: {"description": "Not found"}},
)