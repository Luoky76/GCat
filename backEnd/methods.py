
from datetime import datetime, timedelta
ACTIONTYPE=("push", "commit", "pull", "remote", "merge")

def stemp2str(timeStamp: float):
    """
        将时间戳转为UTC时间字符串
    """
    return datetime.strftime(datetime.utcfromtimestamp(timeStamp), '%Y-%m-%dT%H:%M:%SZ', )


def utc2chn(UTCstr: str):
    """
        将UTC时间字符串转化为北京时间字符串
    """

    # return datetime.strftime(datetime.utcfromtimestamp(datetime.timestamp(datetime.strptime(UTCstr, '%Y-%m-%dT%H:%M:%SZ')))+timedelta(hours=16),'%Y/%m/%d %H:%M:%S')
    stamp = datetime.timestamp(
        datetime.strptime(UTCstr, '%Y-%m-%dT%H:%M:%SZ'))
    UTCtime = datetime.utcfromtimestamp(stamp)
    CHNtime = UTCtime+timedelta(hours=16)
    CHNstr = CHNtime.strftime('%Y/%m/%d %H:%M')
    return CHNstr


def Actionchange(action: dict):
    pass
