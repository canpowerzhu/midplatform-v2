# @Author  : kane.zhu
# @Time    : 2021/7/21 12:14
# @Software: PyCharm
from fastapi import APIRouter,status
from fastapi.encoders import jsonable_encoder
from app import settings
from app.dao import models
from app.module import DataModel
from starlette.responses import JSONResponse

router = APIRouter(
    prefix='/baseconf',
    tags=["baseconf"],
    responses={404:{"description":"Not found"}},
)

@router.get("/",tags=["baseconf"],
            summary="获取内部配置key列表",
            description="内部模块 获取配置的key",
            # response_model=dict[int,str,list],
            status_code=status.HTTP_200_OK)
async  def getconflist(page: int = 1, limit :int = 10):
        try:
            # TODO 分页查询需要支持，结构体返回
            res = await models.tbl_baseconf.all().values_list()
            settings.BaseConfig.RESP_STRUCT['code']= 200
            settings.BaseConfig.RESP_STRUCT['msg']= 'success'
            settings.BaseConfig.RESP_STRUCT['count'] = len(res)
            settings.BaseConfig.RESP_STRUCT['data']= res

        except Exception as e:
            settings.BaseConfig.RESP_STRUCT['msg']= e
        return JSONResponse(jsonable_encoder(settings.BaseConfig.RESP_STRUCT))


@router.get("/{conf_key}",tags=["baseconf"],summary="获取内部配置选项", description="内部模块 获取配置的value")
async  def getconf(conf_key: str):
    pass

@router.put("/{item_id}",tags=["baseconf"], summary="更新内部配置选项", description="内部模块 更新配置")
async  def updateconf(item_id: int):
    pass


@router.post("/",
             tags=["baseconf"],
             summary="新增内部配置选项",
             description="内部模块 新增配置",
             response_model=DataModel.RespStruct,
             status_code=status.HTTP_201_CREATED)
async  def addconf(item: DataModel.Addconf):
        try:
            res = await models.tbl_baseconf.create(**item.dict())
            status = "success"
        except Exception as e:
            print(e)
            status = "failed"
        return {"IsOK":status}



