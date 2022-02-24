# @Author  : kane.zhu
# @Time    : 2022/2/22 15:31
# @Software: PyCharm


from fastapi import status
from fastapi.responses import JSONResponse, Response
from typing import Union


def resp_200(*, data: Union[list, dict, str]) -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 200,
            'msg': "success",
            'data': data
        }
    )


# 自定义异常工具
def resp_400(*, data: str = None, msg: str = "BAD REQUEST") -> Response:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            'code': 400,
            'msg': msg,
            'data': data
        }

    )
