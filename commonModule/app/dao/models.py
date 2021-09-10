# @Author  : kane.zhu
# @Time    : 2021/7/20 21:22
# @Software: PyCharm


from tortoise import models,fields

class tbl_baseconf(models.Model):
    """
    基础配置表
    """
    id = fields.IntField(pk=True)
    name        = fields.CharField(max_length=100,description="配置名称")
    conf_key    = fields.CharField(max_length=100,description="配置键")
    conf_value  = fields.CharField(max_length=500,description="配置值")
    category    = fields.CharField(max_length=500,description="分类")
    description = fields.CharField(null=True,max_length=100,description="描述")
    create_time = fields.DatetimeField(auto_now_add=True,description="创建时间")
    update_time = fields.DatetimeField(auto_now=True,description="更新时间")

    # category conf_key 联合唯一，保证大类里面不重复
    class Meta:
        unique_together = (("category", "conf_key"),)

class tbl_webhoook_log(models.Model):
    """
    钉钉机器人调用记录
    """
    id = fields.IntField(pk=True)
    name            = fields.CharField(max_length=150, description='调用者的名称')
    status           = fields.BooleanField(default=True, description='发送的状态 默认是成功')
    content        = fields.JSONField(max_length=100, description='调用发送的内容')
    create_time     = fields.DatetimeField(auto_now_add=True, description='创建时间')


class tbl_operate_log(models.Model):
    """
    业务操作日志
    """
    traceId  = fields.CharField(pk=True,max_length=100,description="追踪ID，每个用户在线期间的操作日志")
    username = fields.CharField(max_length=300,description="操作的用户名")
    protocol = fields.CharField(max_length=100,description="采用的协议")
    path     = fields.CharField(max_length=500,description="请求路径")
    ip = fields.CharField(max_length=128,description='请求IP地址 设置为128 可支持IPv6')
    params = fields.TextField(blank=True, null=True, description="请求参数")
    status = fields.BooleanField(description='操作状态 0-异常 1-正常')
    operate_type = fields.CharField(max_length=500, description='操作类型 修改 新增 删除等')
    request_time = fields.DatetimeField(auto_now_add=True,description='请求时间')

class tbl_login_out(models.Model):
    """
    登录登出相关日志
    """
    traceId = fields.CharField(pk=True,max_length=100,description='登陆时 产生一个traceId')
    username = fields.CharField(max_length=100,description='用户名')
    status = fields.BooleanField(description='登陆状态 0-失败 1-成功')
    ip = fields.CharField(max_length=128,description='请求IP地址 设置为128 可支持IPv6')
    os_type = fields.CharField(max_length=200, description='操作系统类型')
    broswer_type = fields.CharField(max_length=100, description='浏览器类型')
    broswer_version = fields.CharField(max_length=100, description='浏览器版本')
    user_agent = fields.CharField(max_length=500, description='useragent信息')
    action = fields.BooleanField(description='0-登出 1-登陆')
    request_time = fields.DatetimeField(auto_now_add=True,description='请求时间')

class tbl_apklist(models.Model):
    """
    apk保存相关
    """
    project_name = fields.CharField(max_length=100,description='所属项目名称')
    package_name = fields.CharField(max_length=100,description='包名')
    verison = fields.CharField(max_length=10,description='版本')
    version_code = fields.IntField(max_length=18,description='版本号')
    env_type = fields.IntField(description="0-正式环境;1-预发布环境;2-测试环境")
    size = fields.BigIntField(max_length=10, description='apk文件大小')
    owner = fields.CharField(max_length=50, description='操作人')
    file_path = fields.CharField(max_length=500, description='文件相对路径')
    create_time = fields.DatetimeField(auto_now_add=True,description='请求时间')