from GEvent import GEvent
import UserInfo


def EventDistributer(gEvent: GEvent)->GEvent:
    if gEvent.eType == "GetInfo":
        
        return GetInfoEventHandler(gEvent)

def GetInfoEventHandler(gEvent: GEvent)->GEvent:
    if "actionList" in gEvent.eDetail:
        (gEvent.eDetail)["actionList"] = UserInfo.getActionList(
            userID=gEvent.userID, earlyTime=gEvent.eTime)
    return gEvent
