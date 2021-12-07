from methods import *
from github import Github

ACTIONTYPES = ("push", "commit", "pull", "remote", "merge")


def getNewRepository(usrtoken: str,
                     earlytime: Optional[float] = 0.0
                     ) -> dict:
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
        if repo.created_at >= earlytime:
            newrepolist.append(repo.url)
        else:
            break

    return {"count": len(newrepolist), "repoList": newrepolist}


def getActionList(usrtoken: str,
                  earlytime: Optional[float],
                  actionkind: Optional[Union[str, set]] = ACTIONTYPES
                  ) -> dict:
    """ 获取用户在 earlytime 后最新的操作&时间信息
        :param usrtoken:用户token
        :param earlytime:查找时间起点
        :param actionkind:指定类型
        :return:{"count":newEventsCount,"eventList":newEventList}
    """

    earlytime = datetime.utcfromtimestamp(earlytime)  # 时间格式化
    newEventList = []  # 创建actionList空列表

    repos = Github(usrtoken).get_user().get_repos()

    for repo in repos:
        if earlytime <= repo.updated_at:
            events = repo.get_events()
            for event in events:
                if earlytime <= event.created_at:
                    action = action_extract(event)
                    if action and action["Type"] in actionkind:
                        newEventList.append(action)

    newEventList.sort(key=lambda e: e["Time"], reverse=True)
    return {"count": len(newEventList), "eventList": newEventList}

def getMyRepos(token)->list:
    """ getMyRepos(token)\n
        获取指定仓库代码文件
        :param token:用户口令
        :return:返回一个列表
    """
    user = Github(token).get_user()
    repos = []
    for repo in user.get_repos(type = "owner"):
        print(repo)
        repos.append(repo.full_name)
    return repos

def getCollRepos(token)->list:
    """ getMyRepos(token)\n
        获取指定仓库代码文件
        :param token:用户口令
        :return:返回一个列表
    """
    user = Github(token).get_user()
    repos = []
    for repo in user.get_repos(type = "collaborator"):
        repos.append(repo.full_name)
    return repos

def getStarRepos(token)->list:
    """ getMyRepos(token)\n
        获取指定仓库代码文件
        :param token:用户口令
        :return:返回一个列表
    """
    user = Github(token).get_user()
    repos = []
    for repo in user.get_starred():
        repos.append(repo.full_name)
    return repos

def getAvatar(token)->str:
    user = Github(token).get_user()
    return user.avatar_url

if __name__ == '__main__':
    # g = Github("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")
    # for repo in g.get_user().get_repos(type = "owner"):
    #     print(repo.full_name)
    # print(getMyRepos("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"))
    pass
