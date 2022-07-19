# @Author  : kane.zhu
# @Time    : 2022/2/24 14:30
# @Software: PyCharm


from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.status import HTTP_401_UNAUTHORIZED
from app.conf import setting
from app.module import schema_user
from app.utils.check_login import get_current_active_user, authenticate_user, create_access_token
from app.dao.models import User

router = APIRouter(
    prefix="/api/v1/login",
    tags=["login"],
    responses={404: {"description": "Not found"}}
)


@router.post("/token", response_model=schema_user.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    real_data = await User.filter(username=form_data.username).first().values()
    user = authenticate_user({form_data.username: real_data}, form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=setting.PrdConfig.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token, refresh_token = create_access_token(data={"username": user.username},
                                                      expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer", "refresh_token": refresh_token}


@router.get("/users/me/", response_model=schema_user.User)
async def read_users_me(current_user: schema_user.User = Depends(get_current_active_user)):
    return current_user
