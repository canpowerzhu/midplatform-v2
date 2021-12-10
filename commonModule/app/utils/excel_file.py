# @Author  : kane.zhu
# @Time    : 2021/12/9 20:50
# @Software: PyCharm

import xlwings as xw
import time
from app.utils import oss_operate
from pathlib import Path


def write_excel(app_name, func_name, data):
    """
    :param app_name: 应用名称
    :param func_name: 功能名称
    :param data: 数据
    :return:
    """
    excel_name = app_name + '_' + func_name + '_' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.xlsx'
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.add()
    try:
        sht = wb.sheets['Sheet1']
        sht.range('A1').value = data
        try:
            wb.save(excel_name)
        except Exception as e:
            print("ee" + str(e))
    finally:
        wb.close()
        app.kill()
    # 判断文件是否存在，上传返回url
    if Path(excel_name).is_file():
        _, res = oss_operate.uploadExcel(excel_name)
    return res
