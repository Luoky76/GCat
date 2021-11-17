
from datetime import datetime, timedelta
from typing import Tuple


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


def ActionExtract(action: dict) -> tuple:
    """
        从动作json字典指定actionKind提取（类型,时间）元组
    """
    ActionType = None
    ActionTime = None

    if action["type"] == "PushEvent":
        ActionType = "push"
        ActionTime = utc2chn(action["created_at"])

    elif action["type"] == "PullRequestEvent":
        if (action["payload"]["pull_request"]["merged_at"] != None):
            ActionType = "merge"
            ActionTime = utc2chn(
                action["payload"]["pull_request"]["merged_at"])

    if ActionType and ActionTime:
        return [ActionType, ActionTime]
    else:
        return None
