# @Author  : kane.zhu
# @Time    : 2022/2/18 16:52
# @Software: PyCharm

from fastapi import APIRouter, Depends, HTTPException
from app.module import schema_user, schema_response
from app.utils import response_code, check_login
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

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


@router.post("/user/token", response_model=schema_user.Token,summary="创建登陆用户的访问token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # 获取的请求体数据
    fake_db = {}
    user = check_login.authenticate_user(fake_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=check_login.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = check_login.create_access_token(
        data={"sub": schema_user.UserCreate.username, "scopes": form_data.scopes},
        expires_delta=access_token_expires
    )

    return {"acess_token": access_token, "token_type": "bearer"}
