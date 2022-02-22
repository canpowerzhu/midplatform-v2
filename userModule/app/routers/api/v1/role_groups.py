# @Author  : kane.zhu
# @Time    : 2022/2/18 16:54
# @Software: PyCharm

# 角色组
from fastapi import  APIRouter

router = APIRouter(
    prefix='/role_groups',
    tags=["role_groups"],
    responses={404: {"description": "Not found"}},
)