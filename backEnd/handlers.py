from gevent import GEvent
from github import Github
from repositoryrcmd import RepositoryRcmd
import UserInfo


def EventDistributer(EventRequest: GEvent)->GEvent:
    if EventRequest.eType == "GetInfo":
        return GetInfoEventHandler(EventRequest)
    elif EventRequest.eType == "Recommend":
        return RecommendEventHandler(EventRequest)

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