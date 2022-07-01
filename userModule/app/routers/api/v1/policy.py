# @Author  : kane.zhu
# @Time    : 2022/2/18 17:07
# @Software: PyCharm


from fastapi import APIRouter
from app.module import schema_policy
from app.utils import response_code

router = APIRouter(
    prefix="/api/v1",
    tags=["policy"],
    responses={404: {"description": "Not found"}}
)


@router.get("/policy/list",
            summary="获取权限列表", description="权限列表")
async def get_policy():
    return {"code": 200, "msg": "success"}


@router.get("/policy/{policy_id}",
            summary="获取权限信息", description="获取权限信息")
async def get_policy_info():
    return {"code": 200, "msg": "success"}


@router.post("/policy", summary="新建权限")
async def create_policy(body: schema_policy.Policy):
    return response_code.resp_200(data=dict(body))


@router.put("/policy/{policy_id}",
            summary="更新角色信息", description="更新角色信息")
async def update_policy_info():
    return {"code": 200, "msg": "success"}
