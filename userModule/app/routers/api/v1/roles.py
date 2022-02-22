# @Author  : kane.zhu
# @Time    : 2022/2/18 16:53
# @Software: PyCharm
from fastapi import APIRouter
from app.utils import response_code
from app.module import schema_role

router = APIRouter(
    prefix='/api/v1',
    tags=["roles"],
    responses={404: {"description": "Not found"}},
)


@router.get("/role/list",
            summary="获取角色列表", description="角色列表")
async def get_role():
    return {"code": 200, "msg": "success"}


@router.get("/role/{role_id}",
            summary="获取角色信息", description="获取角色信息")
async def get_role_info():
    return {"code": 200, "msg": "success"}


@router.post("/role", summary="新建角色")
async def create_user(body: schema_role.RoleCreate):
    return response_code.resp_200(data=dict(body))


@router.put("/role/{role_id}",
            summary="更新角色信息", description="更新角色信息")
async def update_role_info():
    return {"code": 200, "msg": "success"}