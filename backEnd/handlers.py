from gevent import GEvent
from github import Github
from repositoryrcmd import RepositoryRcmd
import UserInfo
import GitHubOperator


def EventDistributer(EventRequest: GEvent)->GEvent:
    if EventRequest.eType == "GetInfo":
        return GetInfoEventHandler(EventRequest)
    elif EventRequest.eType == "Recommend":
        return RecommendEventHandler(EventRequest)
    elif EventRequest.eType == "GetFileList":
        return GetFileListHandler(EventRequest)
    elif EventRequest.eType == "GetFile":
        return GetFileHandler(EventRequest)
    elif EventRequest.eType == "CheckStar":
        return CheckStarHandler(EventRequest)
    elif EventRequest.eType == "Star":
        return StarHandler(EventRequest)
    elif EventRequest.eType == "DeclineStar":
        return DeclineStarHandler(EventRequest)
    elif EventRequest.eType == "Follow":
        return FollowHandler(EventRequest)
    elif EventRequest.eType == "DeclineFollow":
        return DeclineFollowHandler(EventRequest)

def GetInfoEventHandler(gEvent: GEvent)->GEvent:
    if "actionList" in gEvent.eDetail:
        (gEvent.eDetail)["actionList"] = UserInfo.getActionList(
            gEvent.userID, gEvent.eTime)
    return gEvent

def RecommendEventHandler(gEvent: GEvent)->GEvent:
    g = Github(gEvent.token)
    obj = RepositoryRcmd(g)
    gEvent.eDetail = obj.getRcmd(g)
    return gEvent

def GetFileListHandler(gEvent: GEvent)->GEvent:
    res = UserInfo.getRepoContent(gEvent.userID, gEvent.eDetail["reponame"])
    gEvent.eDetail = res
    return gEvent

def GetFileHandler(gEvent: GEvent)->GEvent:
    res = UserInfo.getRepoContent(gEvent.userID, gEvent.eDetail["reponame"], gEvent.eDetail["filepath"], gEvent.eDetail["type"])
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
