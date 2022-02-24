# @Author  : kane.zhu
# @Time    : 2021/7/1 11:46
# @Software: PyCharm
from urllib.request import Request

import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.conf import setting
from app.routers.api.v1 import roles, user_groups, users, role_groups

app = FastAPI(title="Mop DevOps", description="运维中台", version=2.0)
app.include_router(router=users.router)
app.include_router(router=user_groups.router)
app.include_router(router=roles.router)
app.include_router(router=role_groups.router)

register_tortoise(app, config=setting.ORM_LINK_CONF, generate_schemas=True)

if __name__ == '__main__':
    uvicorn.run(app="main:app", host=setting.Config.SERVER_HOST, port=setting.Config.SERVER_PORT, reload=True)
