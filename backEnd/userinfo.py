import requests
from methods import *
from github import Github

ActionTypes = ("push", "commit", "pull", "remote", "merge")
UserEventsApi = "https://api.github.com/users/{}/events"


def getNewRepository(usrtoken: str, earlyTime: float) -> int:
    """
        获取 用户userID 在 指定时间earlyTime 后创建的仓库数量
        :param usrtoken:用户token
        :param earlyTime:查找时间起点
        :return:仓库数量
    """
    newRepoList=[]
    repoList = Github(usrtoken).get_user().get_repos(
        sort="creatd", direction="desc")  # 获取json数据
    earlyTime = datetime.fromtimestamp(earlyTime)  # 时间格式化
    for repo in repoList:
        print(repo.url)
        if repo.created_at >= earlyTime:
            newRepoList.append(repo.url)
        else:
            break

    return {"count":len(newRepoList),"repoList":newRepoList}


def getActionList(usrtoken: str, earlyTime: float, actionKind: str = ActionTypes) -> list:
    """ getActionList(userID,earlyTime[,actionKind])\n
        获取用户最近操作&时间二维表``[[事件类型，发生时间],...]``
        :param usrtoken:用户token
        :param earlyTime:查找时间起点
        :param actionKind:指定类型
        :return:返回一个列表
    """
    earlyTime = stemp2str(earlyTime)  # 时间格式化

    newEventList = []  # 创建actionList空列表

    userID = Github(usrtoken).get_user().login  # 获取用户名
    eventList = requests.get(UserEventsApi.format(userID)).json()  # 获取json数据

    for action in eventList:
        if earlyTime <= action["created_at"]:  # earlyTime之后发生
            Action = ActionExtract(action)
            if Action and Action["Type"] in actionKind:
                newEventList.append(Action)

    return {"count":len(newEventList),"eventList":newEventList}

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
