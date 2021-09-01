# @Author  : kane.zhu
# @Time    : 2021/7/9 18:06
# @Software: PyCharm

import uvicorn
from fastapi import FastAPI, APIRouter, HTTPException,Header


# register_tortoise APP对象和操作的数据库绑定在一起
from tortoise.contrib.fastapi import register_tortoise
from routers import  baseconf,encrypto

app = FastAPI()
# 加解密相关
app.include_router(encrypto.router)
# 基础配置相关
app.include_router(baseconf.router)


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")



register_tortoise(app,
                  db_url="mysql://root:Mop@WSx12po!4QAZ@192.168.1.5:3306/zhu",
                  modules={"models": ['dao.models']},
                  add_exception_handlers=True, #生产环境不要开，会泄露调试信息
                  generate_schemas=True #如果数据库为空，则自动生成对应表单,生产环境不要开
                )

if __name__ == '__main__':
    uvicorn.run(app="main:app", host="127.0.0.1", port=5000, reload=True)
