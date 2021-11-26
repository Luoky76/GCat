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
<<<<<<< HEAD
    elif gEvent.etype == "CreateRepo":
        return Create_repoEventHandler(gEvent)
=======
    elif gEvent.etype == "ChangeUserInfo":
        return ChangeUserInfoHandler(gEvent)
>>>>>>> b8ebabae108a23f3b57e1fc893d447860447c7b9


def GetInfoHandler(gEvent: GEvent) -> GEvent:
    """
        返回对象.eDetail["信息"]=所求信息
    """
    if "newEvents" in gEvent.edetail:
        gEvent.edetail["newEvents"] = userinfo.getActionList(
            gEvent.token, gEvent.etime)
    if "newRepos" in gEvent.edetail:
        gEvent.edetail["newRepos"] = userinfo.getNewRepository(
            gEvent.token, gEvent.etime)
    if "myrepos" in gEvent.edetail:
        gEvent.edetail["myrepos"] = userinfo.getMyRepos(gEvent.token)
    return gEvent


def RecommendHandler(gEvent: GEvent) -> GEvent:
    """
        返回对象.eDtail=推荐仓库列表
    """
    g = Github(gEvent.token)
    obj = RepositoryRcmd(g)
    gEvent.edetail = obj.getRcmd(g)
    return gEvent


def GetFileListHandler(gEvent: GEvent) -> GEvent:
    res = userinfo.getRepoContent(
<<<<<<< HEAD
        gEvent.edetail["username"], gEvent.edetail["reponame"], gEvent.token)
=======
        gEvent.edetail["username"], gEvent.edetail["reponame"], gEvent.etype)
>>>>>>> b8ebabae108a23f3b57e1fc893d447860447c7b9
    gEvent.edetail = res
    return gEvent

def GetFileHandler(gEvent: GEvent) -> GEvent:
<<<<<<< HEAD
    res = userinfo.getRepoContentDetail(
        gEvent.edetail["username"], gEvent.edetail["reponame"], gEvent.edetail["filepath"], gEvent.edetail["type"], gEvent.token)
=======
    res = userinfo.getRepoContent(
        gEvent.edetail["username"], gEvent.edetail["reponame"], gEvent.edetail["filepath"], gEvent.edetail["type"], gEvent.etype)
>>>>>>> b8ebabae108a23f3b57e1fc893d447860447c7b9
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

<<<<<<< HEAD
def Create_repoEventHandler(gEvent: GEvent) -> GEvent:
    if GitHubOperator.create_repo(gEvent.edetail["reponame"], gEvent.edetail["file_dict"], gEvent.token):
        gEvent.edetail = "success"
=======
def ChangeUserInfoHandler(gEvent: GEvent) -> GEvent:
    if "follow" in gEvent.edetail:
        if GitHubOperator.follower(gEvent.edetail["follow"], gEvent.token):
            gEvent.edetail["follow"] = "success"
        else:
            gEvent.edetail["follow"] = "error"

    if "declineFollow" in gEvent.edetail:
        if GitHubOperator.declineFollower(gEvent.edetail["declineFollow"], gEvent.token):
            gEvent.edetail["declineFollow"] = "success"
        else:
            gEvent.edetail["declineFollow"] = "error"

    if "star" in gEvent.edetail:
        if GitHubOperator.declineStar(gEvent.edetail["star"], gEvent.token):
            gEvent.edetail["star"] = "success"
        else:
            gEvent.edetail["star"] = "error"

    if "declineStar" in gEvent.edetail:
        if GitHubOperator.declineStar(gEvent.edetail["declineStar"], gEvent.token):
            gEvent.edetail["declineStar"] = "success"
        else:
            gEvent.edetail["declineStar"] = "error"

    if "checkStar" in gEvent.edetail:
        if GitHubOperator.checkstar(gEvent.edetail["checkStar"], gEvent.token):
            gEvent.edetail["checkStar"] = "yes"
        else:
            gEvent.edetail["checkStar"] = "no"

>>>>>>> b8ebabae108a23f3b57e1fc893d447860447c7b9
    return gEvent