# @Author  : kane.zhu
# @Time    : 2021/12/10 20:05
# @Software: PyCharm

from fastapi import APIRouter,status
from app.module import DataModel
from app.utils import webhook_dingtalk
import json

router = APIRouter(
    prefix='/webhook',
    tags=["webhook"],
    responses={404: {"description": "Not found"}},
)


@router.post("/baseconf",
             tags=["baseconf"],
             summary="新增内部配置选项",
             description="内部模块 新增配置",
             response_model_exclude_none=True,
             status_code=status.HTTP_200_OK)
async def send_dingtalk(item:DataModel.Webhook_Data):
        hook = webhook_dingtalk.Webhook(item.token,item.secret)
        status, resp_body = hook.send(json.dumps(item.send_content))
        return {"code": status, "message": resp_body}