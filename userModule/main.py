# @Author  : kane.zhu
# @Time    : 2021/7/1 11:46
# @Software: PyCharm
import uvicorn
from fastapi import FastAPI

app = FastAPI()
@app.get("/user",summary="用户接口", description="用户接口描述")
async def user(example={'userId': "必填，格式是number类型"}):
    return  {"message":"hello world"}

if __name__ == '__main__':
    uvicorn.run(app="main:app",host="127.0.0.1", port=5001, reload=True)
