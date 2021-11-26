from datetime import datetime, timedelta
from typing import Optional, Union
from github.Event import Event
import jieba.posseg


def dataprepos(text: str, stopkey: list) -> list[str]:
    """ 文本预处理，返回指定词性的词
        :param text:待处理字符串
        :param stopkey:停用词列表
        :return:筛选后字符串列表
    """
    wordList = []
    pos = ['n', 'nz', 'v', 'vd', 'vn', 'l', 'a', 'd']  # 定义选取的词性
    seg = jieba.posseg.cut(text)  # 文本切割
    for i in seg:
        if i.word not in stopkey and i.flag in pos:  # 去停用词 + 词性筛选
            wordList.append(i.word)
    return wordList


def stemp2str(timeStamp: float) -> str:
    """ 将时间戳转为UTC时间字符串
        :param timeStamp:待转换时间戳
        :return:Github时间字符串
    """
    return datetime.strftime(datetime.utcfromtimestamp(timeStamp), '%Y-%m-%dT%H:%M:%SZ')


def utc2cst(UTCtime: Union[datetime, str]) -> str:
    """ 将UTC时间datetimeH或str类型转化为CST时间字符串
        :param UTCtime:UTC时间
        :return:CST时间字符串 '%Y/%m/%d %H:%M:%S'
    """
    if type(UTCtime) == str:
        CSTstr = (datetime.strptime(
            UTCtime, '%Y-%m-%dT%H:%M:%SZ')+timedelta(hours=8)
        ).strftime('%Y/%m/%d %H:%M:%S')
    else:
        CSTstr = (UTCtime+timedelta(hours=8)).strftime('%Y/%m/%d %H:%M:%S')
    return CSTstr


def action_extract(action: Event) -> dict:
    """ 从动作json字典指定actionKind提取（类型,时间）元组
        :param action:事件字典
        :return:{"Type": ActionType, "Time": ActionTime, "Repo": ActionRepo}
    """
    actype = None
    actime = None
    acrepo = None
    acactor = None

    if action.type == "PushEvent":
        actype = "push"
        actime = utc2cst(action.created_at)

    elif action.type == "PullRequestEvent":
        if (action.payload["pull_request"]["merged_at"] != None):
            actype = "merge"
            actime = utc2cst(action.payload["pull_request"]["merged_at"])

    acrepo = {
        "name": action.repo.name,
        "url": action.repo.url,
    }

    acactor = {"login": action.actor.login,
               "avatar_url": action.actor.avatar_url, "url": action.actor.url}

    if actype and actime and acrepo:
        return {"Type": actype, "Time": actime, "Repo": acrepo, "actor": acactor}
    else:
        return None
