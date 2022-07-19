# @Author  : kane.zhu
# @Time    : 2022/2/21 17:33
# @Software: PyCharm


from app.utils import check_login
from tortoise.models import Model

from app.dao import models as userModel


def db_create_user(user_db) -> bool:
    result = await userModel.User.create(**user_db)
    print(result)
    return True
