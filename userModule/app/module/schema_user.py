# @Author  : kane.zhu
# @Time    : 2022/2/21 17:49
# @Software: PyCharm
import re

from pydantic import BaseModel, Field, validator, EmailStr
from typing import Optional, List
from datetime import datetime


class UserCreate(BaseModel):
    nickname: str
    username: str
    group_id: int
    avatar: str
    gender: int
    email: EmailStr
    phone: Optional[str] = Field(None, regex=r'^[0-9]\d{11}$', title="手机号")
    # 0-禁用,1-启用,2-强制启用
    mfa_level: int = Field(0, ge=0, le=2, description="mfa_level value must in 0-2")
    otp_secret_key: Optional[str]
    private_key: Optional[str] = None
    public_key: Optional[str] = None
    comment: Optional[str]
    created_by: int
    is_active: Optional[bool] = True
    last_login: bool
    expire_time: datetime = None

    # # 用户名校验只包含数字字母
    # @validator('username')
    # def name_only_contain(cls, v):
    #     assert v.isalnum(), 'must be alphanumeric'
    #     return v


# 查，删，改，
class User(UserCreate):
    id: int
    create_time: str
    update_time: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
    scopes: List[str] = []


class UserInDB(UserCreate):
    hashed_password: str
