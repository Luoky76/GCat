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

def create_repo(repoID:str ,file_dict:dict, token) -> bool:
    """创建仓库"""
    g = Github(token)
    user = g.get_user()
    repo = user.create_repo(repoID)
    for source_repo_name in file_dict.keys():
        source_repo = g.get_repo(source_repo_name)
        for item in file_dict[source_repo_name]:
            content = source_repo.get_contents(item)
            repo.create_file(content.path, "初始化", content.decoded_content)
    return True

def search_repo(token, reponame):
    g = Github(token)
    list = []
    for repo in g.search_repositories(reponame):
        list.append(repo.full_name)
    return list
if __name__ == '__main__':
    # g = Github("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")
    # repo = g.get_repo("sindresorhus/awesome")
    # print(type(repo))
    # print(type(repo.get_issue(1)))
    # print(repo.get_issue(1).title)
    # print(repo.get_issue(1).user)
    # pass
    # g = Github("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")
    # source_repo = g.get_repo("ShakingSH/CPP_Test")
    # content = source_repo.get_contents("test.c")
    # # print(type(content))
    # # print(content.path)
    # repo = g.get_repo("ShakingSH/10.26test")
    # repo.create_file(content.path, "初始化", content.decoded_content)
    # create_repo("createtest4", {"ShakingSH/CPP_Test":["test.c", "test2.cpp", "code_test.cpp"]}, "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")
    # g = Github("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")
    # user = g.get_user()
    # repo = user.create_repo("createtest7")
    # file_list = ["ShakingSH/CPP_Test/test.c", "ShakingSH/CPP_Test/test2.cpp", "ShakingSH/CPP_Test/code_test.cpp"]
    # for path in file_list:
    #     content = repo.get_contents(path)
    #     repo.create_file(content.path, "初始化", content.decoded_content)
    g = Github("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")
    print(g.search_repositories("ShakingSH"))
    for repo in g.search_repositories("ShakingSH"):
        print(repo.full_name)
    pass
