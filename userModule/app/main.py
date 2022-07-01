# @Author  : kane.zhu
# @Time    : 2021/7/1 11:46
# @Software: PyCharm
from urllib.request import Request

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from tortoise.contrib.fastapi import register_tortoise
from app.conf import setting
from app.routers.api.v1 import roles, user_groups, users, role_groups, login, policy

app = FastAPI(title="MopDevOps", description="运维中台之用户模块", version=2.0)
app.include_router(router=users.router)
app.include_router(router=user_groups.router)
app.include_router(router=roles.router)
app.include_router(router=role_groups.router)
app.include_router(router=policy.router)
app.include_router(router=login.router)

# 由于路由问题 重定向到对应接口
@app.post("/token")
async def redirect_back():
    return RedirectResponse("/api/v1/login/token")


register_tortoise(app, config=setting.ORM_LINK_CONF, generate_schemas=True)

if __name__ == '__main__':
    uvicorn.run(app="main:app", host=setting.Config.SERVER_HOST, port=setting.Config.SERVER_PORT, reload=True)
