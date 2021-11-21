from gevent import GEvent
from github import Github
from repositoryrcmd import RepositoryRcmd
import userinfo
import GitHubOperator


def EventDistributer(EventRequest: GEvent) -> GEvent:
    """
        根据GEvent.eType将需求分发给对应函数
        返回对象包含所求信息
    """
    if EventRequest.eType == "GetInfo":
        return GetInfoEventHandler(EventRequest)
    elif EventRequest.eType == "Recommend":
        return RecommendEventHandler(EventRequest)


def GetInfoEventHandler(gEvent: GEvent) -> GEvent:
    """
        返回对象.eDetail["信息"]=所求信息
    """
    if "newEvents" in gEvent.eDetail:
        gEvent.eDetail["newEvents"] = userinfo.getActionList(
            gEvent.token, gEvent.eTime)
    if "newRepos" in gEvent.eDetail:
        gEvent.eDetail["newRepos"] = userinfo.getNewRepository(
            gEvent.token, gEvent.eTime)
    return gEvent


def RecommendEventHandler(gEvent: GEvent) -> GEvent:
    """
        返回对象.eDtail=推荐仓库列表
    """
    g = Github(gEvent.token)
    obj = RepositoryRcmd(g)
    gEvent.eDetail = obj.getRcmd(g)
    return gEvent

def GetFileListHandler(gEvent: GEvent)->GEvent:
    res = userinfo.getRepoContent(gEvent.eDetail["username"], gEvent.eDetail["reponame"])
    gEvent.eDetail = res
    return gEvent

def GetFileHandler(gEvent: GEvent)->GEvent:
    res = userinfo.getRepoContent(gEvent.eDetail["username"], gEvent.eDetail["reponame"], gEvent.eDetail["filepath"], gEvent.eDetail["type"])
    gEvent.eDetail = res
    return gEvent

def StarHandler(gEvent: GEvent)->GEvent:
    if GitHubOperator.star(gEvent.eDetail["full_name"], gEvent.token):
        gEvent.eDetail = "success"
    else:
        gEvent.eDetail = "failed"
    return gEvent

def DeclineStarHandler(gEvent: GEvent)->GEvent:
    if GitHubOperator.declineStar(gEvent.eDetail["full_name"], gEvent.token):
        gEvent.eDetail = "success"
    else:
        gEvent.eDetail = "failed"
    return gEvent

def CheckStarHandler(gEvent: GEvent)->GEvent:
    if GitHubOperator.checkstar(gEvent.eDetail["full_name"], gEvent.token):
        gEvent.eDetail = "yes"
    else:
        gEvent.eDetail = "no"
    return gEvent

def FollowHandler(gEvent: GEvent)->GEvent:
    if GitHubOperator.follower(gEvent.userID, gEvent.token):
        gEvent.eDetail = "success"
    else:
        gEvent.eDetail = "failed"
    return gEvent

def DeclineFollowHandler(gEvent: GEvent)->GEvent:
    if GitHubOperator.declineFollower(gEvent.userID, gEvent.token):
        gEvent.eDetail = "success"
    else:
        gEvent.eDetail = "failed"
    return gEvent
