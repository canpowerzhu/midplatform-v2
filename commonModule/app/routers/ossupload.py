# @Author  : kane.zhu
# @Time    : 2021/8/31 14:43
# @Software: PyCharm

from fastapi import APIRouter, status, File, UploadFile

from app.module import DataModel
from app.utils import OssOps, unPack
from tempfile import NamedTemporaryFile
import shutil
from pathlib import Path

router = APIRouter(
    prefix='/ossupload',
    tags=["ossupload"],
    responses={404: {"description": "Not found"}},
)


@router.post("/uploadpic", tags=["ossupload"],
             summary="上传图片至oss",
             description="以base64方式上传图片",
             # response_model=dict[int,str,list],
             status_code=status.HTTP_200_OK)
async def upload_pic(item: DataModel.OssPicReq):
    _, res = OssOps.uploadBase64Pic(item.dict()['base64pic'])
    return {"code": 200, "url": res}


@router.post("/makeexcel", tags=["ossupload"],
             summary="生成excel并上传至oss",
             description="传json数据",
             # response_model=dict[int,str,list],
             status_code=status.HTTP_200_OK)
async def make_excel(item: DataModel.OssExcelReq):
    # TODO 生成excel文件流待完成，传入数据流返回url
    # OssOps.uploadExcel(file, filename="test.excel")
    return {"code": 200, "url": "res"}


@router.post("/uploadapk", tags=["ossupload"],
             summary="上传apk至oss",
             description="以文件流的方式上传apk",
             status_code=status.HTTP_200_OK)
async def upload_apk(file: UploadFile = File(...)):
    "上传apk至oss"
    import os
    with NamedTemporaryFile(delete=False, suffix=Path(file.filename).suffix, dir='tmp/') as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_file_name = Path(tmp.name).name
    file.file.close()
    apk = unPack.parse_apk("tmp/" + tmp_file_name)
    _, accessurl = OssOps.uploadApk("tmp/" + tmp_file_name, file.filename)
    resp_data = {}
    resp_data['package_name'] = apk.package_name
    resp_data['version_code'] = apk.version_code
    resp_data['version_name'] = apk.version_name
    resp_data['package_size'] = os.path.getsize("tmp/" + tmp_file_name)
    resp_data['accessurl'] = accessurl

    return {"code": 200, "url": resp_data}
