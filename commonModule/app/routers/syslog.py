# @Author  : kane.zhu
# @Time    : 2021/8/31 14:43
# @Software: PyCharm
import datetime

from fastapi import APIRouter, status, Query
from app.module import DataModel
from app.dao import models
from app.settings import BaseConfig
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional

router = APIRouter(
    prefix='/log',
    tags=["log"],
    responses={404: {"description": "Not found"}},
)


@router.post("/login_out", tags=["log"],
             summary="日志相关",
             description="登陆登出日志")
async def login_out(item: DataModel.LoginOut):
    try:
        await  models.tbl_login_out.create(**item.dict())
        code = status.HTTP_201_CREATED
        message = 'success'
    except Exception as e:
        print(e)
        message = 'fail'
        code = status.HTTP_400_BAD_REQUEST

    BaseConfig.POST_DATA['code'] = code
    BaseConfig.POST_DATA['message'] = message
    return JSONResponse(jsonable_encoder(BaseConfig.POST_DATA))


@router.get("/login_out", tags=["log"],
            summary="日志相关",
            # response_model=DataModel.LoginOut,
            response_model_include={'id', 'request_time'},
            description="登陆登出日志,系统调用")
# 用户名查询，登陆IP，时间范围，状态(正常异常)，动作类型（登陆登出），traceId
async def get_login_out(current_page: int = 1,
                        show_size: int = 10,
                        username: Optional[str] = Query(None),
                        ip: Optional[str] = Query(None),
                        start_time: Optional[datetime.datetime] = Query(None),
                        end_time: Optional[datetime.datetime] = Query(None),
                        action: Optional[bool] = Query(None),
                        trace_id: Optional[str] = Query(None),
                        status: Optional[bool] = Query(None)):
    QuerySet = {}
    # 如果没有结束时间，则结束时间为现在
    if start_time != None and end_time == None:
        end_time = datetime.datetime.now()

    # 判断时间范围，开始时间小于结束时间，并小于现在
    if start_time.__lt__(end_time) and end_time.__lt__(datetime.datetime.now()):
        print("time_range_ok")

    if ip is not None:
        QuerySet['ip'] = ip

    if trace_id is not None:
        QuerySet['trace_id'] = trace_id

    if username is not None:
        QuerySet['username'] = username

    if action is not None:
        QuerySet['action'] = action

    if status is not None:
        QuerySet['status'] = status

    res= await  models.tbl_login_out.all().values_list()
    print(res)
    # print(current_page, show_size, username, ip, start_time, end_time, action, trace_id, status)
    return {"plaintext": "res_dict", "ciphertext": "ciphertext"}


@router.post("/operate", tags=["log"],
             summary="操作日志相关",
             description="操作日志")
async def operate_log(example={'plaintext': "必填，格式是string类型"}):
    return {"plaintext": "res_dict", "ciphertext": "ciphertext"}


@router.get("/operate", tags=["log"],
            summary="操作日志相关",
            description="操作日志")
async def get_operate_log(example={'plaintext': "必填，格式是string类型"}):
    return {"plaintext": "res_dict", "ciphertext": "ciphertext"}


@router.get("/webhook", tags=["log"],
            summary="webhook日志",
            description="webhook日志")
async def get_webhook_log(example={'plaintext': "必填，格式是string类型"}):
    return {"plaintext": "res_dict", "ciphertext": "ciphertext"}


@router.post("/webhook", tags=["log"],
             summary="webhook日志",
             description="webhook日志")
async def webhook_log(example={'plaintext': "必填，格式是string类型"}):
    return {"plaintext": "res_dict", "ciphertext": "ciphertext"}
