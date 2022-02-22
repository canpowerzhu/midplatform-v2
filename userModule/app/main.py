# @Author  : kane.zhu
# @Time    : 2021/7/1 11:46
# @Software: PyCharm
import uvicorn
from fastapi import FastAPI
from app.routers.api.v1 import roles, user_groups, users, role_groups

app = FastAPI()

app.include_router(router=users.router)
app.include_router(router=user_groups.router)
app.include_router(router=roles.router)
app.include_router(router=role_groups.router)

if __name__ == '__main__':
    uvicorn.run(app="main:app",host="127.0.0.1", port=5001, reload=True)
