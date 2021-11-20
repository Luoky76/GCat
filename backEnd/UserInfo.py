import requests
import time
from methods import *
from github import Github

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

def getRepoContent(username, reponame) ->dict:
    """ getRepoContent(username, reponame)\n
        获取指定仓库代码文件
        :param username:用户名
        :param reponame:仓库名
        :return:返回一个字典{文件路径：文件类型}
    """
    g = Github()
    user = g.get_user(username)
    repo = user.get_repo(reponame)
    file_dict = {}
    for content in repo.get_contents(""):
        file_dict[content.path] = content.type
    return file_dict

def getRepoContentDetail(username, reponame, filepath, type):
    """ getRepoContentDetail(username, reponame, filepath, type)\n
        获取指定仓库代码文件
        :param username:用户名
        :param reponame:仓库名
        :param filepath:文件路径
        :param type:文件类型
        :return:返回一个字符串 or 一个字典{文件路径：文件类型}，视文件类型而定
    """
    g = Github()
    user = g.get_user(username)
    repo = user.get_repo(reponame)
    content = repo.get_contents(filepath)
    file_dict = {}
    if type == "file":
        return content.decoded_content
    elif type == "dir":
        for in_content in content:
            file_dict[in_content.name] = in_content.type
        return file_dict
