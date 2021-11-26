from github import Github
import github.NamedUser
import requests
import time
from github.Repository import Repository


def follower(otheruserID: str, token) -> bool:
    """获取用户关注"""
    g = Github(token)
    user = g.get_user()
    if user.has_in_following(otheruserID):
        return False
    else:
        user.add_to_following()
        return True


def declineFollower(otheruserID: str, token) -> bool:
    """取消用户关注"""
    g = Github(token)
    user = g.get_user()
    if user.has_in_following(otheruserID):
        user.remove_from_following(otheruserID)
        return True
    else:
        return False


def star(repoID: str, token) -> bool:
    """收藏"""
    g = Github(token)
    user = g.get_user()
    if user.has_in_starred(g.get_repo(repoID)):
        return False
    else:
        user.add_to_starred(g.get_repo(repoID))
        return True


def declineStar(repoID: str, token) -> bool:
    """取关"""
    g = Github(token)
    user = g.get_user()
    if user.has_in_starred(g.get_repo(repoID)):
        user.remove_from_starred(g.get_repo(repoID))
        return True
    else:
        return False


def checkstar(repoID: str, token) -> bool:
    """收藏"""
    g = Github(token)
    user = g.get_user()
    if user.has_in_starred(g.get_repo(repoID)):
        return True
    else:
        return False


def getissue(repoID: str):
    return


def create_repo(repoID) -> str:
    """创建仓库"""
    pass
