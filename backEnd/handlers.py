from gevent import GEvent
from github import Github
from datetime import datetime, timedelta
from reposrcmd import RepositoryRcmd
import userinfo
import repoinfo
import GitHubOperator
import dbmethod


def EventDistributer(gEvent: GEvent) -> GEvent:
    """
        根据GEvent.eType将需求分发给对应函数
        返回对象包含所求信息
    """
    if gEvent.etype == "GetInfo":
        return GetInfoHandler(gEvent)
    elif gEvent.etype == "Recommend":
        return RecommendHandler(gEvent)
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
    elif gEvent.etype == "GetRepoInfo":
        return GetRepoInfoHandler(gEvent)
    elif gEvent.etype == "CreateRepo":
        return Create_repoEventHandler(gEvent)
    elif gEvent.etype == "GetRepoMsg":
        return GetRepoMsgHandler(gEvent)
    elif gEvent.etype == "GetRepoReadme":
        return GetRepoReadmeHandler(gEvent)
    elif gEvent.etype == "GetUserAvatar":
        return GetUserAvatarHandler(gEvent)
    elif gEvent.etype == "SetHistory":
        return SetHistoryHandler(gEvent)
    elif gEvent.etype == "GetHistory":
        return GetHistoryHandler(gEvent)
    elif gEvent.etype == "SearchRepo":
        return SearchRepoHandler(gEvent)


def GetInfoHandler(gEvent: GEvent) -> GEvent:
    """
        返回对象.eDetail["信息"]=所求信息
    """
    timefrom = (datetime.now()-timedelta(days=7)).timestamp()

    if "newEvents" in gEvent.edetail:
        if gEvent.edetail["newEvents"] != None:
            if "type" in gEvent.edetail["newEvents"]:
                typereqest = gEvent.edetail["newEvents"]["type"]
            if "time" in gEvent.edetail["newEvents"]:
                timefrom = gEvent.edetail["newEvents"]["time"]
            gEvent.edetail["newEvents"] = userinfo.getActionList(
                gEvent.token, timefrom, typereqest)
        else:
            gEvent.edetail["newEvents"] = userinfo.getActionList(
                gEvent.token, timefrom)
    if "newRepos" in gEvent.edetail:
        gEvent.edetail["newRepos"] = userinfo.getNewRepository(
            gEvent.token, timefrom)
    if "myrepos" in gEvent.edetail:
        gEvent.edetail["myrepos"] = userinfo.getMyRepos(gEvent.token)
    if "collrepos" in gEvent.edetail:
        gEvent.edetail["collrepos"] = userinfo.getCollRepos(gEvent.token)
    if "starrepos" in gEvent.edetail:
        gEvent.edetail["starrepos"] = userinfo.getStarRepos(gEvent.token)
    return gEvent


def RecommendHandler(gEvent: GEvent) -> GEvent:
    """
        返回对象.eDtail=推荐仓库列表
    """
    g = Github(gEvent.token)
    obj = RepositoryRcmd(g)
    gEvent.edetail = obj.getRcmd(g)
    print(gEvent.edetail)
    return gEvent


def GetFileListHandler(gEvent: GEvent) -> GEvent:
    res = repoinfo.getRepoContent(
        gEvent.edetail["username"], gEvent.edetail["reponame"], gEvent.token)
    gEvent.edetail = res
    return gEvent

def GetFileHandler(gEvent: GEvent) -> GEvent:
    res = repoinfo.getRepoContentDetail(
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

def GetRepoInfoHandler(gEvent: GEvent):
    if "pull_request_list" in gEvent.edetail:
        gEvent.edetail["pull_request_list"] = repoinfo.getPullrequet(
            gEvent.token, gEvent.edetail["full_name"])
    if "collaborator_list" in gEvent.edetail:
        gEvent.edetail["collaborator_list"] = repoinfo.getCollaborator(
            gEvent.token, gEvent.edetail["full_name"])

    return gEvent

def Create_repoEventHandler(gEvent: GEvent) -> GEvent:
    if GitHubOperator.create_repo(gEvent.edetail["reponame"], gEvent.edetail["file_dict"], gEvent.token):
        gEvent.edetail = "success"
    return gEvent

def GetRepoMsgHandler(gEvent: GEvent) -> GEvent:
    gEvent.edetail["msg"] = repoinfo.getrepodetail(gEvent.token, gEvent.edetail["full_name"])
    return gEvent

def GetRepoReadmeHandler(gEvent: GEvent) -> GEvent:
    gEvent.edetail["msg"] = repoinfo.getreporeadme(gEvent.token, gEvent.edetail["full_name"])
    print(gEvent.edetail["msg"])
    return gEvent

def GetUserAvatarHandler(gEvent: GEvent) -> GEvent:
    gEvent.edetail = userinfo.getAvatar(gEvent.token)
    return gEvent

def SetHistoryHandler(gEvent: GEvent) -> GEvent:
    gEvent.edetail = dbmethod.inserthistory(gEvent.token,gEvent.edetail["full_name"])
    return gEvent

def GetHistoryHandler(gEvent: GEvent) -> GEvent:
    gEvent.edetail = dbmethod.searchhistory(gEvent.token)
    return gEvent

def SearchRepoHandler(gEvent: GEvent) -> GEvent:
    gEvent.edetail = GitHubOperator.search_repo(gEvent.token, gEvent.edetail["name"])
    return gEvent
