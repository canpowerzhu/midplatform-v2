# @Author  : kane.zhu
# @Time    : 2022/3/2 19:01
# @Software: PyCharm

import redis
from app.conf import setting

r = redis.Redis()


class OpsRedis(object):
    """
    redis operate  for standalone
    """
    def __init__(self, redis_host, redis_passwd, redis_port, redis_db):
        try:
            self.r = redis.Redis(host=redis_host, password=redis_passwd,
                                 port=redis_port, db=redis_db)
        except Exception as e:
            print("redis初始化连接失败，错误%s" % e)

    def get_value(self, key):
        get_res = self.r.get(key)
        if not get_res:
            return get_res.decode()

    def del_key(self, key):
        return self.r.delete(key)

    def set_key(self, key, value, time=None):
        return self.r.set(key, value, time)

    # property把方法直接转成属性使用
    @property
    def clean_redis(self):
        self.r.flushdb()
        return 0

    # 把update_expire_time变成静态方法， 与OpsRedis截开，不再有类的属性
    @classmethod
    def update_expire_time(cls):
        print("the result is %s", cls)
        # self.r.set(key,value,time)
