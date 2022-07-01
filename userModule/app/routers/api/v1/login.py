# @Author  : kane.zhu
# @Time    : 2022/2/24 14:30
# @Software: PyCharm
from datetime import timedelta

from fastapi import APIRouter, Security, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.status import HTTP_401_UNAUTHORIZED

from app.conf import setting
from app.module import schema_user
from app.utils.check_login import get_current_active_user, get_current_user, authenticate_user, create_access_token

router = APIRouter(
    prefix="/api/v1/login",
    tags=["login"],
    responses={404: {"description": "Not found"}}
)

fake_users_db = {
    "kane.zhu": {
        "username": "kane.zhu",
        "gender": True,
        "avatar": "/img/user/1.jpg",
        "phone": 18121443665,
        "mfa_devel": 0,
        "is_active": True,
        "group_id": 2,
        "email": "kane.zhu@moppomobi.com",
        "hashed_password": "$2b$12$166Kra0.D8qR1TKa/K4Dj.KRWTwEtFrhfJvdfv.4V6wei.DkGxNoO",
        "disabled": False,
    }
}


# 登陆，返回token
@router.post("/token", response_model=schema_user.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # 验证密码并校验
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or passowrd",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=setting.PrdConfig.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token, refresh_token = create_access_token(data={"username": user.username},
                                                      expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer", "refresh_token": refresh_token}
    # , "attributes": "", "expires_ttl": 56563}


@router.get("/users/me/", response_model=schema_user.User)
async def read_users_me(current_user: schema_user.User = Depends(get_current_active_user)):
    return current_user
