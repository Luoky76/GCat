import requests
from methods import *

ACTIONTYPE = ("push", "commit", "pull", "remote", "merge")

def getActionList(userID: str, earlyTime: float, actionKind:str = ACTIONTYPE) -> tuple:
    """
        获取用户最近操作&时间二维表``[[事件类型，发生时间],...]``
        :param userID:用户名
        :param earlyTime:查找时间起点
        :param actionKind:指定类型
        :return:返回一个列表
    """
    data = requests.get("https://api.github.com/users/" +
                        userID+"/events").json()  # 获取json数据
    earlyTime = stemp2str(earlyTime)  # 时间格式化
    actionList = []  # 创建actionList空列表

    for action in data:
        if earlyTime <= action["created_at"]:  # earlyTime之后发生
            Action = ActionExtract(action)
            if Action and Action[0] in actionKind:
                actionList.append(Action)

    return actionList


