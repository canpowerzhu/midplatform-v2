# @Author  : kane.zhu
# @Time    : 2022/2/23 23:04
# @Software: PyCharm


from starlette.config import Config as StarletConfig
import os
from collections import OrderedDict

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
config = StarletConfig(os.path.join(os.path.dirname(os.path.dirname(BASE_PATH)), '.env'))


#######################################################################################

class BaseConfig(object):
    ######################################################################################
    # encrypt key & offset
    PASSKEY = config('PASSKEY', default='')
    PASSOFFSET = config('PASSOFFSET', default='')
    SECRET_KEY = config('SECRET_KEY', default='')
    #######################################################################################
    # server start param
    SERVER_HOST = config('SERVER_HOST', default='127.0.0.1')
    SERVER_PORT = config('SERVER_PORT', cast=int, default=5001)
    # Response Body struct
    GET_DATA = OrderedDict()
    POST_DATA = OrderedDict()
    GET_DATA = {
        'code': int,
        'show_size': int,
        'current_page': int,
        'count': int,
        'records': ''
    }
    POST_DATA = {
        'code': int,
        'message': str
    }

    #######################################################################################
    # INCLUDE_IN_SCHEMA = config('INCLUDE_IN_SCHEMA', cast=bool, default=True)
    #######################################################################################
    # ORM
    def _get_orm_base_conf(self, appd: dict) -> dict:
        return {
            'connections': {
                'default': {
                    'engine': 'tortoise.backends.mysql',
                    'credentials': {
                        'host': self.DB_HOST,
                        'port': self.DB_PORT,
                        'user': self.DB_USER,
                        'password': self.DB_PASSWD,
                        'database': self.DB_DATABASE,
                        'minsize': 1,
                        'maxsize': self.DB_MAX_SIZE,
                        'charset': 'utf8mb4'
                    }
                }
            },
            'apps': appd,
            'use_tz': False,
            'timezone': 'Asia/Shanghai'
        }

    @property
    def orm_link_conf(self) -> dict:
        orm_apps_settings = {
            'models': {
                'models': [
                    'app.dao.models'
                ],
                'default_connection': 'default',
            }
        }
        return self._get_orm_base_conf(orm_apps_settings)


class PrdConfig(BaseConfig):
    ###################################################################################################################
    # redis
    REDIS_HOST = config('REDIS_HOST', default='127.0.0.1')
    REDIS_PORT = config('REDIS_PORT', cast=int, default=6379)
    REDIS_PASSWD = config('REDIS_PASSWD', default='')
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    ###################################################################################################################
    # mysql database
    DB_USER = config('DB_USER', default='root')
    DB_PASSWD = config('DB_PASSWD', default='')
    DB_HOST = config('DB_HOST', default='127.0.0.1')
    DB_PORT = config('DB_PORT', cast=int, default=3306)
    DB_DATABASE = config('DB_DATABASE', default='')
    DB_MAX_SIZE = config('DB_MAX_SIZE', cast=int, default=5)
    # print("部分参数",DB_PASSWD,DB_HOST,DB_DATABASE)

    ALGORITHM = config('ALGORITHM', default="HS256")


Config = PrdConfig
ORM_LINK_CONF = Config().orm_link_conf
