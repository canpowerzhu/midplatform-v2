# @Author  : kane.zhu
# @Time    : 2022/2/18 16:52
# @Software: PyCharm

from fastapi import APIRouter, status
from app.module import schema_user, schema_response
from app.utils import response_code

router = APIRouter(
    prefix='/api/v1',
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/user/list",
            summary="获取用户列表", description="用户列表")
async def get_user():
    return {"code": 200, "msg": "success"}


@router.get("/user/{user_id}",
            summary="获取用户信息", description="获取用户信息")
async def get_user_info():
    return {"code": 200, "msg": "success"}


@router.post("/user", summary="新建用户")
async def create_user(body: schema_user.UserCreate):
    return response_code.resp_200(data=dict(body))


@router.put("/user/{user_id}",
            summary="更新用户信息", description="更新用户信息")
async def update_user_info():
    return {"code": 200, "msg": "success"}
