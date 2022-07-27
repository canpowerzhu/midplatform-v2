# @Author  : kane.zhu
# @Time    : 2021/7/21 12:14
# @Software: PyCharm
from fastapi import APIRouter, status, Query
from fastapi.encoders import jsonable_encoder
from app.settings import BaseConfig
from app.dao import models
from app.module import datamodel as DataModel
from starlette.responses import JSONResponse
from typing import Optional

router = APIRouter(
    prefix='/baseconf',
    tags=["baseconf"],
    responses={404: {"description": "Not found"}},
)


@router.get("/baseconf", tags=["baseconf"],
            summary="获取内部配置key列表",
            description="内部模块 获取配置的key",
            response_description="success")
async def get_conf_list(current_page: int = 1, show_size: int = 10):
    try:
        res = await  models.tbl_baseconf.get().limit(show_size).offset(current_page - 1).values_list()
        code = status.HTTP_200_OK
        count = len(res)
    except Exception as e:
        code = status.HTTP_400_BAD_REQUEST
    BaseConfig.GET_DATA['code'] = code
    BaseConfig.GET_DATA['show_size'] = show_size
    BaseConfig.GET_DATA['current_page'] = current_page
    BaseConfig.GET_DATA['count'] = count
    BaseConfig.GET_DATA['records'] = res
    return JSONResponse(jsonable_encoder(BaseConfig.GET_DATA))


@router.get("/baseconf/search", tags=["baseconf"], summary="获取内部配置选项", description="内部模块 获取配置的value")
async def get_conf(current_page: int = 1,
                   show_size: int = 10,
                   category: Optional[str]=Query(None),
                   conf_key: Optional[str]=Query(None)):
    search = {}
    if category != None:
        search['category'] = category
    if conf_key != None:
        search['conf_key'] = conf_key
    try:
        res = await models.tbl_baseconf.filter(**search).values_list()
        code = status.HTTP_200_OK
        count = len(res)
    except Exception as e:
        code = status.HTTP_400_BAD_REQUEST
    BaseConfig.GET_DATA['code'] = code
    BaseConfig.GET_DATA['show_size'] = show_size
    BaseConfig.GET_DATA['current_page'] = current_page
    BaseConfig.GET_DATA['count'] = count
    BaseConfig.GET_DATA['records'] = res
    return JSONResponse(jsonable_encoder(BaseConfig.GET_DATA))




@router.put("/baseconf/{item_id}", tags=["baseconf"], summary="更新内部配置选项", description="内部模块 更新配置")
async def update_conf(item_id: int, items: DataModel.Addconf):
    try:
        await models.tbl_baseconf.filter(pk=item_id).update(**items)
        code = status.HTTP_200_OK
        message = 'success'
    except Exception as e:
        message = 'fail'
        code = status.HTTP_400_BAD_REQUEST
    BaseConfig.POST_DATA['code'] = code
    BaseConfig.POST_DATA['message'] = message

    return JSONResponse(jsonable_encoder(BaseConfig.POST_DATA))


@router.post("/baseconf",
             tags=["baseconf"],
             summary="新增内部配置选项",
             description="内部模块 新增配置",
             response_model_exclude_none=True,
             status_code=status.HTTP_201_CREATED)
async def add_conf(item: DataModel.Addconf):
    try:
        await models.tbl_baseconf.create(**item.dict())
        message = "success"
        code = status.HTTP_201_CREATED
    except Exception as e:
        print(e)
        message = "failed"
    BaseConfig.POST_DATA['code'] = code
    BaseConfig.POST_DATA['message'] = message
    return JSONResponse(jsonable_encoder(BaseConfig.POST_DATA))
