# @Author  : kane.zhu
# @Time    : 2021/9/7 10:17
# @Software: PyCharm

import time, calendar, base64, oss2

from app import settings

# 定义file文件名，以及相关子路径命名
ts = str(calendar.timegm(time.gmtime()))
subdir = time.strftime("%Y%m%d", time.localtime())

# 初始化oss相关对象
auth = oss2.Auth(settings.Config.ACCESSKEY, settings.Config.ACCESSSECRET)
bucket = oss2.Bucket(auth, settings.Config.ENDPOINT, settings.Config.BUCKETNAME)


def percentage(consumed_bytes, total_bytes):
    if total_bytes:
        rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
        print('\r{0}% '.format(rate), end='')


def uploadApk(file, filename):
    """
    :param file: 本地临时文件
    :return:
    """
    accessurl = 'midplatform-v2/ApkDir/' + subdir + '/' + ts + '_' + filename
    # 这个是阿里提供的SDK方法 bucket是调用的4.1中配置的变量名
    try:
        bucket.put_object_from_file(accessurl, file, progress_callback=percentage)
    except Exception as err:
        return False, err
    return True, accessurl


def uploadBase64Pic(data):
    b64_data = data.split(';base64,')[1]
    logoType = data.split(';base64,')[0].split('/')[1]
    data = base64.b64decode(b64_data)
    # 定义上传时间戳（second级别）
    remotePath = 'midplatform-v2/image/' + subdir + '/' + ts + '.' + logoType
    try:
        bucket.put_object(remotePath, data)
    except Exception as err:
        return False, err
    return True, remotePath


def uploadExcel(file,filename):
    accessurl = 'midplatform-v2/excel/' + subdir + '/' + ts + '_' + filename
    # 这个是阿里提供的SDK方法 bucket是调用的4.1中配置的变量名
    try:
        bucket.put_object_from_file(accessurl, file, progress_callback=percentage)
    except Exception as err:
        return False, err
    return True, accessurl

