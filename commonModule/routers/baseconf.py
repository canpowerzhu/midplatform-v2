# @Author  : kane.zhu
# @Time    : 2021/7/21 12:14
# @Software: PyCharm
from fastapi import APIRouter
from dao import models
from module import DataModel


router = APIRouter(
    prefix='/baseconf',
    tags=["baseconf"],
    responses={404:{"description":"Not found"}},
)

@router.get("/baseconf",tags=["baseconf"],summary="获取内部配置key列表", description="内部模块 获取配置的key")
async  def getconflist(page: int = 1, limit :int = 10):
    conf = Conf.BaseConf
    res = conf.getAll()


@router.get("/baseconf/{conf_key}",tags=["baseconf"],summary="获取内部配置选项", description="内部模块 获取配置的value")
async  def getconf(conf_key: str):
    pass

@router.put("/baseconf/{item_id}",tags=["baseconf"], summary="更新内部配置选项", description="内部模块 更新配置")
async  def updateconf(item_id: int):
    pass

@router.post("/baseconf",tags=["baseconf"],summary="新增内部配置选项", description="内部模块 新增配置")
async  def addconf(item: DataModel.Addconf):
        # print(item,type(item))
        # data = DataModel.Addconf(**item)
        await models.tbl_baseconf.create(**item.dict())
        # print(item,type(item))
        # conf = Conf.BaseConf()
        # conf.addconf(item)
        pass



