# @Author  : kane.zhu
# @Time    : 2021/7/1 11:46
# @Software: PyCharm
import uvicorn
from fastapi import FastAPI
from routers import users,usergroups,roles,rolegroups

app = FastAPI()

app.include_router(router=users.router)
app.include_router(router=usergroups.router)
app.include_router(router=roles.router)
app.include_router(router=rolegroups.router)

if __name__ == '__main__':
    uvicorn.run(app="main:app",host="127.0.0.1", port=5001, reload=True)
