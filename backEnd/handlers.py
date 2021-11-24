from gevent import GEvent
from github import Github
from reposrcmd import RepositoryRcmd
import userinfo
import GitHubOperator


def EventDistributer(gEvent: GEvent) -> GEvent:
    """
        根据GEvent.eType将需求分发给对应函数
        返回对象包含所求信息
    """
    if gEvent.etype == "GetInfo":
        return GetInfoEventHandler(gEvent)
    elif gEvent.etype == "Recommend":
        return RecommendEventHandler(gEvent)
    elif gEvent.etype == "GetFileList":
        return GetFileListHandler(gEvent)
    elif gEvent.etype == "GetFile":
        return GetFileHandler(gEvent)
    elif gEvent.etype == "CheckStar":
        return CheckStarHandler(gEvent)
    elif gEvent.etype == "Star":
        return StarHandler(gEvent)
    elif gEvent.etype == "DeclineStar":
        return DeclineStarHandler(gEvent)
    elif gEvent.etype == "Follow":
        return FollowHandler(gEvent)
    elif gEvent.etype == "DeclineFollow":
        return DeclineFollowHandler(gEvent)


def GetInfoEventHandler(gEvent: GEvent) -> GEvent:
    """
        返回对象.eDetail["信息"]=所求信息
    """
    if "newEvents" in gEvent.edetail:
        gEvent.edetail["newEvents"] = userinfo.getActionList(
            gEvent.token, gEvent.etime)
    if "newRepos" in gEvent.edetail:
        gEvent.edetail["newRepos"] = userinfo.getNewRepository(
            gEvent.token, gEvent.etime)
    return gEvent


def RecommendEventHandler(gEvent: GEvent) -> GEvent:
    """
        返回对象.eDtail=推荐仓库列表
    """
    g = Github(gEvent.token)
    obj = RepositoryRcmd(g)
    gEvent.edetail = obj.getRcmd(g)
    return gEvent


def GetFileListHandler(gEvent: GEvent) -> GEvent:
    res = userinfo.getRepoContent(
        gEvent.edetail["username"], gEvent.edetail["reponame"], gEvent.token)
    gEvent.edetail = res
    return gEvent


def GetFileHandler(gEvent: GEvent) -> GEvent:
    res = userinfo.getRepoContentDetail(
        gEvent.edetail["username"], gEvent.edetail["reponame"], gEvent.edetail["filepath"], gEvent.edetail["type"], gEvent.token)
    gEvent.edetail = res
    return gEvent


def StarHandler(gEvent: GEvent) -> GEvent:
    if GitHubOperator.star(gEvent.edetail["full_name"], gEvent.token):
        gEvent.edetail = "success"
    else:
        gEvent.edetail = "failed"
    return gEvent


def DeclineStarHandler(gEvent: GEvent) -> GEvent:
    if GitHubOperator.declineStar(gEvent.edetail["full_name"], gEvent.token):
        gEvent.edetail = "success"
    else:
        gEvent.edetail = "failed"
    return gEvent


def CheckStarHandler(gEvent: GEvent) -> GEvent:
    if GitHubOperator.checkstar(gEvent.edetail["full_name"], gEvent.token):
        gEvent.edetail = "yes"
    else:
        gEvent.edetail = "no"
    return gEvent


def FollowHandler(gEvent: GEvent) -> GEvent:
    if GitHubOperator.follower(gEvent.userID, gEvent.token):
        gEvent.edetail = "success"
    else:
        gEvent.edetail = "failed"
    return gEvent


def DeclineFollowHandler(gEvent: GEvent) -> GEvent:
    if GitHubOperator.declineFollower(gEvent.userID, gEvent.token):
        gEvent.edetail = "success"
    else:
        gEvent.edetail = "failed"
    return gEvent
