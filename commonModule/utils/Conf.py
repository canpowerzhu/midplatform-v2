# @Author  : kane.zhu
# @Time    : 2021/7/31 17:41
# @Software: PyCharm
from dao import models
class BaseConf():
    def getAll():
        res = models.BaseConf.get()
        print(res)
        return True



