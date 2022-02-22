# @Author  : kane.zhu
# @Time    : 2022/2/22 16:56
# @Software: PyCharm
from pydantic import BaseModel, Field
from typing import Optional


class UserGroupCreate(BaseModel):
    group_name: str
    is_active: bool
    created_by: int
    comment: Optional[str] = None
