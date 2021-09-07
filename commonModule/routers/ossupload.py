# @Author  : kane.zhu
# @Time    : 2021/8/31 14:43
# @Software: PyCharm
import time

from fastapi import APIRouter, status, File, UploadFile
from module import DataModel
from utils import OssOps,unPack
from tempfile import NamedTemporaryFile
import shutil
from pathlib import Path

router = APIRouter(
    prefix='/ossupload',
    tags=["ossupload"],
    responses={404: {"description": "Not found"}},
)


@router.post("/ossupload/uploadpic", tags=["ossupload"],
             summary="上传图片至oss",
             description="以base64方式上传图片",
             # response_model=dict[int,str,list],
             status_code=status.HTTP_200_OK)
async def uploadpic(item: DataModel.OssPicReq):
    _, res = OssOps.uploadBase64Pic(item.dict()['base64pic'])
    return {"code": 200, "url": res}


@router.post("/ossupload/uploadapk", tags=["ossupload"],
             summary="上传apk至oss",
             description="以文件流的方式上传apk",
             status_code=status.HTTP_200_OK)
async def uploadapk(file: UploadFile=File(...)):
    "上传apk至oss"

    with NamedTemporaryFile(delete=False, suffix=Path(file.filename).suffix, dir='tmp/') as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_file_name = Path(tmp.name).name
    file.file.close()
    apk = unPack.parse_apk("tmp/" + tmp_file_name)
    _, accessurl =   OssOps.uploadApk("tmp/" + tmp_file_name,file.filename)
    print(accessurl, apk.package_name, apk.version_name, apk.version_code)


    return {"code": 200,"filename": file.filename,"filetype": file.content_type}
