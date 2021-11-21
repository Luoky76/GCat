from github import Github
import github.NamedUser
import requests
import time
from github.Repository import Repository

# g = Github('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')
# username = 'fireflylxx'

# user = g.get_user()
# Actions = ('follow', 'declineFollow', 'star', 'declineStar')
# creat_type = ('CreatRepo', 'DropRepo')
#
# repo = user.get_repos()
# following = user.get_following()
# star = user.get_starred()
# print(type(g.get_repo("Luoky76/GCat")))
# print(type(user))
# user.add_to_starred(g.get_repo("Luoky76/GCat"))
# user.create_repo("new-test")
# user.add_to_starred(g.get_repo("Luoky76/GCat"))
# FollowReposApi = 'https:api.github.com/users/{}/followers'
# StarReposApi = 'https:api.github.com/users/{}/starred'
# ReposApi = 'https:api.github.com/users/{}/repos'
#
# data = {
#     "eventID": 422743327,
#     "userID": "fireflylxx",
#     "userToken": "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",
#     "eType": "ChangeUserInfo",
#     "eDetail": {
#         "follow": "fireflylxx",
#         "declineFollow": "ShakingSH",
#         "star": "Luoky76/Gcat",
#         "declineStar": "Luoky76/GCatDoc"
#     },
#     "eTime": 125599946663.62
# }


def follower(otheruserID:str, token) -> bool:
    """获取用户关注"""
    g = Github(token)
    user = g.get_user()
    if user.has_in_following(otheruserID):
        return False
    else:
        user.add_to_following()
        return True


def declineFollower(otheruserID:str, token) -> bool:
    """取消用户关注"""
    g = Github(token)
    user = g.get_user()
    if user.has_in_following(otheruserID):
        user.remove_from_following(otheruserID)
        return True
    else:
        return False


def star(repoID:str, token) -> bool:
    """收藏"""
    g = Github(token)
    user = g.get_user()
    if user.has_in_starred(g.get_repo(repoID)):
        return False
    else:
        user.add_to_starred(g.get_repo(repoID))
        return True


def declineStar(repoID:str, token) -> bool:
    """取关"""
    g = Github(token)
    user = g.get_user()
    if user.has_in_starred(g.get_repo(repoID)):
        user.remove_from_starred(g.get_repo(repoID))
        return True
    else:
        return False

def checkstar(repoID:str, token) -> bool:
    """收藏"""
    g = Github(token)
    user = g.get_user()
    if user.has_in_starred(g.get_repo(repoID)):
        return True
    else:
        return False

def getissue(repoID:str):
    return

def create_repo(repoID) -> str:
    """创建仓库"""
    pass

if __name__ == '__main__':
    # g = Github("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")
    # repo = g.get_repo("sindresorhus/awesome")
    # print(type(repo))
    # print(type(repo.get_issue(1)))
    # print(repo.get_issues().title)











