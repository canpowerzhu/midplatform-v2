# @Author  : kane.zhu
# @Time    : 2022/2/22 18:33
# @Software: PyCharm
from pydantic import BaseModel,Field
from typing import Optional


class RoleCreate(BaseModel):
    role_name: str
    is_active: bool
    created_by: str
    role_group_id: int
    comment: Optional[str] = None


class RoleGroupCreate(BaseModel):
    role_group_name: str
    is_active: bool
    created_by: str
    comment: Optional[str] = None
