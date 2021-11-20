from gevent import GEvent
from github import Github
from repositoryrcmd import RepositoryRcmd
import UserInfo


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
    if "actionList" in gEvent.eDetail:
        (gEvent.eDetail)["actionList"] = UserInfo.getActionList(
            gEvent.userID, gEvent.eTime)
    return gEvent


def RecommendEventHandler(gEvent: GEvent) -> GEvent:
    """
        返回对象.eDtail=推荐仓库列表
    """
    g = Github(gEvent.token)
    obj = RepositoryRcmd(g)
    gEvent.eDetail = obj.getRcmd(g)
    return gEvent
