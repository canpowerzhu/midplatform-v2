# @Author  : kane.zhu
# @Time    : 2021/7/9 18:06
# @Software: PyCharm


from fastapi import FastAPI, HTTPException, Header
# register_tortoise APP对象和操作的数据库绑定在一起
from tortoise.contrib.fastapi import register_tortoise
from app.routers import encrypto,ossupload,baseconf,syslog,webhook
import settings

app = FastAPI()

# 加解密相关
app.include_router(encrypto.router)
# 基础配置相关
app.include_router(baseconf.router)
# 文件上传相关
app.include_router(ossupload.router)
# 日志相关
app.include_router(syslog.router)
# dingTalk相关
app.include_router(webhook.router)


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


register_tortoise(app, config=settings.ORM_LINK_CONF, generate_schemas=False)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app="main:app", host=settings.Config.SERVER_HOST, port=settings.Config.SERVER_PORT, reload=True)
