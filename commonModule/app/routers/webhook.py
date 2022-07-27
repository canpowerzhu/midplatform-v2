# @Author  : kane.zhu
# @Time    : 2021/12/10 20:05
# @Software: PyCharm

from fastapi import APIRouter, status
from app.module import datamodel as DataModel
from app.utils import webhook_dingtalk, email_hook
import json, os

router = APIRouter(
    prefix='/alarm',
    tags=["alarm"],
    responses={404: {"description": "Not found"}},
)


@router.post("/dingtalk",
             tags=["webhook"],
             summary="钉钉webhook通知",
             description="钉钉webhook通知",
             response_model_exclude_none=True,
             status_code=status.HTTP_200_OK)
async def send_dingtalk(item: DataModel.Webhook_Data):
    dingtalk_obj = webhook_dingtalk.Webhook(item.token, item.secret)
    status, resp_body = dingtalk_obj.send(json.dumps(item.dingtalk_content))
    return {"code": status, "message": resp_body}


@router.post("/email",
             tags=["email"],
             summary="邮件消息通知",
             description="邮件消息通知",
             response_model_exclude_none=True,
             status_code=status.HTTP_200_OK)
async def send_dingtalk(item: DataModel.Email_Data):
    email_obj = email_hook.EmailHook(item.msg_to)
    tempale_html = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                'static/Verification_code.html')

    f = open(tempale_html, 'rb')
    mail_body = f.read()
    f.close()
    update_mail_body = mail_body.decode().replace('{}',item.email_content)
    if email_obj.send(item.email_subject, update_mail_body):
        return {"code": 200, "message": 22}
