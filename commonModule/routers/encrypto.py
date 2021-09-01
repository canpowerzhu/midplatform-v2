# @Author  : kane.zhu
# @Time    : 2021/7/21 12:02
# @Software: PyCharm
from fastapi import APIRouter
from module import DataModel
from utils import PasswordSalt

router = APIRouter(
    prefix='/encrypt',
    tags=["encrypt"],
    responses={404:{"description":"Not found"}},
)


# @app.post("/encrypt",summary="明文加密", description="公共模块 明文加密")
@router.api_route("/Aencrypt", tags=["encrypt"], methods=["POST"], summary="明文加密", description="公共模块 明文加密")
async def Aencrypt(item: DataModel.Plaintext, example={'plaintext': "必填，格式是string类型"}):
    res_dict = item.dict()
    passKey = '=====bWlkcGxhdGZvcm0gYXV0aA====='
    passOffset = 'bWlkcGxhdGZvcm0g'
    obj = PasswordSalt.Aesencrypt(passKey, passOffset)
    ciphertext = obj.encrypt(res_dict['plaintext'])
    return {"plaintext": res_dict['plaintext'], "ciphertext": ciphertext}


@router.api_route("/Dencrypt", tags=["encrypt"], methods=["POST"], summary="密文解密", description="公共模块 密文解密")
async def Dencrypt(item: DataModel.Ciphertext, example={'ciphertext': "必填，格式是string类型"}):
    res_dict = item.dict()
    passKey = '=====bWlkcGxhdGZvcm0gYXV0aA====='
    passOffset = 'bWlkcGxhdGZvcm0g'
    obj = PasswordSalt.Aesencrypt(passKey, passOffset)
    plaintext = obj.decrypt(res_dict['ciphertext'])
    return { "ciphertext": res_dict['ciphertext'],"plaintext": plaintext}