import requests
import time
from methods import *

ActionTypes = ("push", "commit", "pull", "remote", "merge")
UserReposApi = "https://api.github.com/users/{}/repos"
UserEventsApi = "https://api.github.com/users/{}/events"


def getNewRepositoryCnt(userID: str, earlyTime: float) -> int:
    """
        获取 用户userID 在 指定时间earlyTime 后创建的仓库数量
        :param userID:用户名
        :param earlyTime:查找时间起点
        :return:仓库数量
    """
    count = 0
    data = requests.get(UserReposApi.format(userID)).json()  # 获取json数据
    earlyTime = stemp2str(earlyTime)  # 时间格式化
    reposList = [repo for repo in data if earlyTime <= repo["created_at"]]

    return len(reposList)


def getActionList(userID: str, earlyTime: float, actionKind: str = ActionTypes) -> list:
    """ getActionList(userID,earlyTime[,actionKind])\n
        获取用户最近操作&时间二维表``[[事件类型，发生时间],...]``
        :param userID:用户名
        :param earlyTime:查找时间起点
        :param actionKind:指定类型
        :return:返回一个列表
    """
    data = requests.get(UserEventsApi.format(userID)).json()  # 获取json数据
    earlyTime = stemp2str(earlyTime)  # 时间格式化
    actionList = []  # 创建actionList空列表

    for action in data:
        if earlyTime <= action["created_at"]:  # earlyTime之后发生
            Action = ActionExtract(action)
            if Action and Action[0] in actionKind:
                actionList.append(Action)

    return actionList
