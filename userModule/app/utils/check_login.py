# @Author  : kane.zhu
# @Time    : 2022/2/23 15:52
# @Software: PyCharm
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, status, Security
from pydantic import ValidationError
from jose import jwt, JWTError

from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes
)

from app.conf import setting
from app.module import schema_user

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes={"me": "Read information about the current user.", "items": "Read items."},
)


def verify_password(plain_password, hashed_password):
    print("encryed pass here: ", pwd_context.hash(plain_password))
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return schema_user.UserInDB(**user_dict)


# 用户名密码认证校验
def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


# 创建JWT
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    # 传入了按过期时间，否则默认15分钟
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, setting.BaseConfig.ACCESS_SECRET_KEY, algorithm=setting.PrdConfig.ALGORITHM)
    refresh_encoded_jwt = jwt.encode(to_encode, setting.BaseConfig.REFRESH_SECRET_KEY,
                                     algorithm=setting.PrdConfig.ALGORITHM)
    return encoded_jwt, refresh_encoded_jwt


def get_current_user(user_db, security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)):
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = f"Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="cloud not validate credentials",
        headers={"WWW-Authenticate": authenticate_value}
    )
    print(token)
    try:
        payload = jwt.decode(token, setting.Config.SECRET_KEY, algorithms=[setting.Config.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = schema_user.TokenData(scopes=token_scopes, username=username)
        print("assss")
    except (JWTError, ValidationError):
        raise credentials_exception

    user = get_user(user_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough Permission",
                headers={"WWW-Authenticate": authenticate_value},
            )
        return user


def get_current_active_user(
        current_user: schema_user.UserCreate = Depends(get_current_user)
):
    print(current_user.is_active)
    if current_user.is_active:
        raise HTTPException(status_code=400, detail="inactive_user")
    return current_user
