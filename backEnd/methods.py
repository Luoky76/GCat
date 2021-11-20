from datetime import datetime, timedelta
import jieba.posseg


def dataprepos(text: str, stopkey: list) -> list:
    """
        文本预处理，返回指定词性的词
    """
    wordList = []
    pos = ['n', 'nz', 'v', 'vd', 'vn', 'l', 'a', 'd']  # 定义选取的词性
    seg = jieba.posseg.cut(text)  # 文本切割
    for i in seg:
        if i.word not in stopkey and i.flag in pos:  # 去停用词 + 词性筛选
            wordList.append(i.word)
    return wordList


def stemp2str(timeStamp: float):
    """
        将时间戳转为UTC时间字符串
    """
    return datetime.strftime(datetime.utcfromtimestamp(timeStamp), '%Y-%m-%dT%H:%M:%SZ')


def utc2cst(UTCstr: str) -> str:
    """
        将UTC时间字符串转化为CST时间字符串
    """
    UTCtime = datetime.strptime(UTCstr, '%Y-%m-%dT%H:%M:%SZ')
    CHNtime = UTCtime+timedelta(hours=8)
    CHNstr = CHNtime.strftime('%Y/%m/%d %H:%M:%S')
    return CHNstr


def ActionExtract(action: dict) -> tuple:
    """
        从动作json字典指定actionKind提取（类型,时间）元组
    """
    ActionType = None
    ActionTime = None

    if action["type"] == "PushEvent":
        ActionType = "push"
        ActionTime = utc2cst(action["created_at"])

    elif action["type"] == "PullRequestEvent":
        if (action["payload"]["pull_request"]["merged_at"] != None):
            ActionType = "merge"
            ActionTime = utc2cst(
                action["payload"]["pull_request"]["merged_at"])

    if ActionType and ActionTime:
        return [ActionType, ActionTime]
    else:
        return None
