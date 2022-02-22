# @Author  : kane.zhu
# @Time    : 2022/2/22 19:46
# @Software: PyCharm

from pydantic import BaseModel
from typing import Optional


class Auth(BaseModel):
    auth_range: str
    auth_policy_name: str
    policy_type: str
    comment: Optional[str] = None


class Policy(BaseModel):
    auth_policy_name: str
    policy_type: str
    quote_count: int
    comment: Optional[str] = None
