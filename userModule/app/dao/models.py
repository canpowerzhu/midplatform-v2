# @Author  : kane.zhu
# @Time    : 2022/2/24 19:49
# @Software: PyCharm
# @Description: 数据库表结构设计
from typing import Optional

from tortoise import models, fields
from app.utils.check_login import get_password_hash
from app.module.schema_user import UserCreate


class User(models.Model):
    id = fields.IntField(pk=True, index=True)
    nickname = fields.CharField(max_length=30, description="昵称")
    username = fields.CharField(max_length=20, description="用户名")
    password_hash = fields.CharField(max_length=128, description="加密后的密码")
    group_id = fields.IntField(default=1, description="用户所属用户组")
    avatar = fields.CharField(max_length=200, description="用户头像存储地址", null=True)
    gender = fields.BooleanField(description="性别，True-男， False-女", default=True)
    email = fields.CharField(max_length=100, description="电子邮箱")
    phone = fields.CharField(max_length=20,description="手机号码")
    mfa_level = fields.IntField(default=0, description="多因子认证0-禁止，1-启用，2-强制启用")
    otp_secret_key = fields.TextField(description="多因子secret_key", null=True)
    private_key = fields.TextField(description="私钥", null=True)
    public_key = fields.TextField(description="公钥", null=True)
    comment = fields.CharField(max_length="500", description="备注信息", null=True)
    created_by = fields.IntField(description="创建者")
    is_active = fields.BooleanField(index=True, description="是否活跃 True-活跃 False-禁止", default=True)
    last_login = fields.DatetimeField(index=True, description="最近一次的登陆时间")
    create_time = fields.DatetimeField(auto_now_add=True, description="用户创建时间")
    update_time = fields.DatetimeField(auto_now=True, description="更新时间")

    @classmethod
    async def create(cls, user: UserCreate) -> "User":
        user_dict = user.dict()
        password_hash = get_password_hash(password=user.password)
        model = cls(**user_dict, password_hash=password_hash)
        await model.save()
        return model

    class Meta:
        table = "tbl_user"
        unique_together = (
            'username', 'phone', 'email'
        )


class UserGroup(models.Model):
    id = fields.IntField(pk=True, index=True)
    group_name = fields.CharField(max_length=30, description="用户组组名称")
    is_active = fields.BooleanField(default=True, description="用户组是否活跃True-活跃 False-禁用")
    created_by = fields.IntField(null=False, description="是由哪个用户创建")
    comment = fields.CharField(max_length=500, null=False, description="用户组备注")
    create_time = fields.DatetimeField(auto_now_add=True, description="创建时间")
    update_time = fields.DatetimeField(auto_now=True, description="更新时间")

    class Meta:
        table = "tbl_user_group"


class Role(models.Model):
    id = fields.IntField(pk=True, index=True)
    role_name = fields.CharField(max_length=50, description="角色名称")
    is_active = fields.BooleanField(default=True, description="用户组是否活跃True-活跃 False-禁用")
    created_by = fields.IntField(null=False, description="是由哪个用户创建")
    role_group_id = fields.IntField(null=False, description="角色所属哪个角色组")
    comment = fields.CharField(max_length=500, null=False, description="用户组备注")
    create_time = fields.DatetimeField(auto_now_add=True, description="创建时间")
    update_time = fields.DatetimeField(auto_now=True, description="更新时间")

    class Meta:
        table = "tbl_role"
        unique_together = (
            'role_name', 'role_group_id'
        )


class RoleGroup(models.Model):
    id = fields.IntField(pk=True, index=True)
    role_group_name = fields.CharField(max_length=50, description="角色组名称")
    is_active = fields.BooleanField(default=True, description="角色组是否活跃True-活跃 False-禁用")
    created_by = fields.IntField(null=False, description="是由哪个用户创建")
    comment = fields.CharField(max_length=500, null=False, description="用户组备注")
    create_time = fields.DatetimeField(auto_now_add=True, description="创建时间")
    update_time = fields.DatetimeField(auto_now=True, description="更新时间")

    class Meta:
        table = "tbl_role_group"
