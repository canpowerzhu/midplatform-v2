# @Author  : kane.zhu
# @Time    : 2022/2/18 16:52
# @Software: PyCharm

from fastapi import APIRouter, Depends, HTTPException,Security
from app.module.schema_user import UserCreate
from app.utils.logs import  logger
from app.utils.check_login import get_password_hash,oauth2_scheme, get_current_active_user
from app.dao.models import User

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
async def get_user_info(user_id: int = Depends(oauth2_scheme)):
    logger.info("获取用户信息"+ user_id)
    return {"code": 200, "msg": "success"}


@router.post("/user", summary="新建用户")
async def create_user(user_in: UserCreate):
    """
    create new user
    """
    hashed_password = get_password_hash(user_in.password)

    db_user = UserCreate(
        **user_in.create_update_dict(), hashed_password=hashed_password
    )
    res = await User.create(db_user)

    return {"code": 200, "msg": "success", "msg": res}


@router.put("/user/{user_id}",
            summary="更新用户信息", description="更新用户信息")
async def update_user_info():
    return {"code": 200, "msg": "success"}
