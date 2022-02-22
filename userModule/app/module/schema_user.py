# @Author  : kane.zhu
# @Time    : 2022/2/21 17:49
# @Software: PyCharm

from pydantic import BaseModel,Field
from typing import Optional


class UserCreate(BaseModel):
    nickname: str
    username: str
    password: str
    group_id: int
    avatar: str
    gender: int
    email: str
    phone: str
    # 0-禁用,1-启用,2-强制启用
    mfa_level: int = Field(0, ge=0, le=2,description="mfa_level value must in 0-2")
    otp_secret_key: Optional[str]
    private_key: Optional[str]
    public_key: Optional[str]
    comment: Optional[str]
    created_by: int
    is_active: Optional[bool] = True
    is_mfa: bool
    expire_time: str


# 查，删，改，
class User(UserCreate):
    id: int
    create_time: str
    update_time: str

