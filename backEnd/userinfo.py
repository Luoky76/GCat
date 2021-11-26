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
