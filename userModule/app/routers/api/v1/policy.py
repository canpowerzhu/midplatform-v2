# @Author  : kane.zhu
# @Time    : 2022/2/18 17:07
# @Software: PyCharm


from fastapi import APIRouter

app = APIRouter(
    prefix="/api/v1/policy",
    tags=["policy"],
    responses={404: {"description": "Not found"}}
)
