# @Author  : kane.zhu
# @Time    : 2022/2/18 16:53
# @Software: PyCharm
from fastapi import APIRouter
from app.utils import response_code
from app.module import schema_usergroup

router = APIRouter(
    prefix='/api/v1',
    tags=["user_groups"],
    responses={404: {"description": "Not found"}},
)


@router.get("/user_group/list",
            summary="获取用户组列表", description="获取用户组列表")
async def get_user_group():
    return {"code": 200, "msg": "success"}


@router.get("/user_group/{user_group_id}",
            summary="获取用户组信息", description="获取用户组信息")
async def get_user_info():
    return {"code": 200, "msg": "success"}


@router.post("/user_group", summary="新建用户组")
async def create_user_group(body: schema_usergroup.UserGroupCreate):
    return response_code.resp_200(data=dict(body))


@router.put("/user_group/{user_group_id}",
            summary="更新用户组信息", description="更新用户组信息")
async def update_user_group_info():
    return {"code": 200, "msg": "success"}
