# @Author  : kane.zhu
# @Time    : 2022/2/21 17:49
# @Software: PyCharm
# @Description：FastApi 数据模型设计
import re

from pydantic import BaseModel, Field, validator, EmailStr
from typing import Optional, List
from datetime import datetime


class BaseProperties(BaseModel):
    def create_update_dict(self):
        return self.dict(
            exclude_unset=True,
            exclude={"id", "is_active"},
        )


class UserCreate(BaseProperties):
    nickname: str
    username: str
    group_id: int
    password: str
    avatar: Optional[str] = None
    gender: Optional[bool] = True
    email: EmailStr
    phone: Optional[str] = Field(None, max_length=11, regex=r'^[0-9]{11}$', title="手机号")
    # \d{3}\-\d{3, 8}
    # 0-禁用,1-启用,2-强制启用
    mfa_level: int = Field(0, ge=0, le=2, description="mfa_level value must in 0-2")
    otp_secret_key: Optional[str]
    private_key: Optional[str] = None
    public_key: Optional[str] = None
    comment: Optional[str]
    created_by: Optional[int] = 1
    is_active: Optional[bool] = True
    last_login: datetime = None
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


class Attributes(BaseModel):
    permissions: List[str] = []


class Token(BaseModel):
    access_token: str
    token_type: str
    # attributes: Attributes
    # expires_ttl: Optional[int] = None
    refresh_token: Optional[str] = None


class TokenData(BaseModel):
    username: Optional[str] = None
    scopes: List[str] = []


class UserInDB(UserCreate):
    hashed_password: str
