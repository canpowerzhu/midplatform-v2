# @Author  : kane.zhu
# @Time    : 2021/12/9 20:50
# @Software: PyCharm

import xlwings as xw
import time
def write_excel(app_name, func_name, data):
    """
    :param app_name: 应用名称
    :param func_name: 功能名称
    :param data: 数据
    :return:
    """
    app=xw.App(visible=False,add_book=False)
    app.display_alerts=False
    app.screen_updating=False
    wb=app.books.add()
    try:
        sht=wb.sheets['Sheet1']
        sht.range('A1').value='a22'
        try:
            wb.save(r'd:\3.xlsx')
        except Exception as e:
           print(e)
    finally:
        wb.close()
        app.kill()
    return True