from typing import Any
import requests
from methods import *
from github import Github

ACTIONTYPES = ("push", "commit", "pull", "remote", "merge")
USEREVENTAPI = "https://api.github.com/users/{}/events"


def getNewRepository(usrtoken: str, earlytime: float) -> dict:
    """ 获取 用户在指定时间 earlytime 后创建的仓库信息
        :param usrtoken:用户token
        :param earlyTime:查找时间起点
        :return:{"count":newReposCount,"repoList":newRepoList}
    """
    newrepolist = []
    repoList = Github(usrtoken).get_user().get_repos(
        sort="creatd", direction="desc")  # 获取json数据
    earlytime = datetime.fromtimestamp(earlytime)  # 时间格式化
    for repo in repoList:
        print(repo.url)
        if repo.created_at >= earlytime:
            newrepolist.append(repo.url)
        else:
            break

    return {"count": len(newrepolist), "repoList": newrepolist}


def getActionList(usrtoken: str, earlytime: float, actionkind: str = ACTIONTYPES) -> dict:
    """ 获取用户在 earlytime 后最新的操作&时间信息
        :param usrtoken:用户token
        :param earlytime:查找时间起点
        :param actionkind:指定类型
        :return:{"count":newEventsCount,"eventList":newEventList}
    """
    earlytime = stemp2str(earlytime)  # 时间格式化

    newEventList = []  # 创建actionList空列表

    usrid = Github(usrtoken).get_user().login  # 获取用户名
    events = requests.get(USEREVENTAPI.format(usrid)).json()  # 获取json数据

    for event in events:
        if earlytime <= event["created_at"]:  # earlyTime之后发生
            action = action_extract(event)
            if action and action["Type"] in actionkind:
                newEventList.append(action)

    return {"count": len(newEventList), "eventList": newEventList}


def getRepoContent(username, reponame, token) -> dict:
    """ getRepoContent(username, reponame)\n
        获取指定仓库代码文件
        :param username:用户名
        :param reponame:仓库名
        :return:返回一个字典{文件路径：文件类型}
    """
    user = Github(token).get_user(username)
    repo = user.get_repo(reponame)
    file_dict = {}
    for content in repo.get_contents(""):
        file_dict[content.path] = content.type
    return file_dict


def getRepoContentDetail(username, reponame, filepath, type, token) -> Any:
<<<<<<< HEAD
    """ getRepoContentDetail(username, reponame, filepath, type, token)\n
=======
    """ getRepoContentDetail(username, reponame, filepath, type)\n
>>>>>>> b8ebabae108a23f3b57e1fc893d447860447c7b9
        获取指定仓库代码文件
        :param username:用户名
        :param reponame:仓库名
        :param filepath:文件路径
        :param type:文件类型
        :return:返回一个字符串 or 一个字典{文件路径：文件类型}，视文件类型而定
    """
    user = Github(token).get_user(username)
    repo = user.get_repo(reponame)
    content = repo.get_contents(filepath)
    file_dict = {}
    if type == "file":
        return content.decoded_content
    elif type == "dir":
        for in_content in content:
            file_dict[in_content.name] = in_content.type
        return file_dict

<<<<<<< HEAD
def getMyRepos(token)->list:
    """ getMyRepos(token)\n
        获取指定仓库代码文件
        :param token:用户口令
        :return:返回一个列表
    """
    user = Github(token).get_user()
    repos = []
    for repo in user.get_repos(type = "owner"):
        repos.append(repo.url)
    return repos

if __name__ == '__main__':
    # g = Github("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")
    # for repo in g.get_user().get_repos(type = "owner"):
    #     print(repo.full_name)
    print(getMyRepos("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"))
=======
if __name__ == '__main__':
    print(getRepoContent("sindresorhus", "awesome", "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"))
>>>>>>> b8ebabae108a23f3b57e1fc893d447860447c7b9
