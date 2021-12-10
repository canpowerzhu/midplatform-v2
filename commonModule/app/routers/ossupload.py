# @Author  : kane.zhu
# @Time    : 2021/8/31 14:43
# @Software: PyCharm

from fastapi import APIRouter, status, File, UploadFile
from app.module import DataModel
from app.utils import oss_operate, parse_apk,excel_file
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
    _, res = oss_operate.uploadBase64Pic(item.dict()['base64pic'])
    return {"code": 200, "url": res}



@router.post("/makeexcel", tags=["ossupload"],
             summary="生成excel并上传至oss",
             description="传json数据",
             # response_model=dict[int,str,list],
             status_code=status.HTTP_201_CREATED)
async def make_excel(item: DataModel.OssExcelReq):
    # TODO 生成excel文件流待完成，传入数据流返回url
    # OssOps.uploadExcel(file, filename="test.excel")
    access_url = excel_file.write_excel(item.app_name, item.func_name, item.excel_data)
    return {"code": 200, "url": access_url}


@router.post("/uploadapk", tags=["ossupload"],
             summary="上传apk至oss",
             description="以文件流的方式上传apk",
             status_code=status.HTTP_201_CREATED)
async def upload_apk(files: UploadFile = File(...)):
    "上传apk至oss"
    import os

    save_dir = "app/tmp"
    try:
        with NamedTemporaryFile(delete=False, suffix=Path(files.filename).suffix, dir=save_dir) as tmp:
            shutil.copyfileobj(files.file, tmp)
            tmp_file_name = Path(tmp.name).name
    finally:
        files.file.close()
    local_file = save_dir+"/"+tmp_file_name
    apk = parse_apk.parse_apk(local_file)
    _, accessurl = oss_operate.uploadApk(local_file, files.filename)

    resp_data = {}
    resp_data['package_name'] = apk.package_name
    resp_data['version_code'] = apk.version_code
    resp_data['version_name'] = apk.version_name
    resp_data['package_size'] = os.path.getsize(local_file)
    resp_data['accessurl'] = accessurl

    return {"code": 200, "url": resp_data}
