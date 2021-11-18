from GEvent import GEvent
from github import Github
import repositoryrcmd
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
    print(11111)
    obj = repositoryrcmd.Repositoryrcmd(g)
    gEvent.eDetail = obj.getRcmd()
    return gEvent
