# @Author  : kane.zhu
# @Time    : 2022/2/22 16:56
# @Software: PyCharm
from pydantic import BaseModel, Field,validator
from typing import Optional


class UserGroupCreate(BaseModel):
    group_name: Optional[str] = Field(None,regex=r'[A-Z_]')
    is_active: bool
    created_by: int
    comment: Optional[str] = None

