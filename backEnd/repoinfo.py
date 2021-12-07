from typing import Union
import methods
from github import Github
from datetime import datetime
import base64
import codecs


def getRepoContent(username: str, reponame: str,
                   token: str) -> dict:
    """ getRepoContent(username, reponame)\n
        获取指定仓库代码文件
        :param username:用户名
        :param reponame:仓库名
        :return:返回一个字典{文件路径：文件类型}
    """
    user = Github(token).get_user(username)
    repo = user.get_repo(reponame)
    file_dict = {}
    for content in repo.get_contents(""):
        file_dict[content.path] = content.type
    return file_dict


def getRepoContentDetail(username: str, reponame: str,
                         filepath: str, type: str, token: str
                         ) -> Union[str, dict]:
    """ getRepoContentDetail(username, reponame, filepath, type)\n
        获取指定仓库代码文件
        :param username:用户名
        :param reponame:仓库名
        :param filepath:文件路径
        :param type:文件类型
        :return:返回一个字符串 or 一个字典{文件路径：文件类型}，视文件类型而定
    """
    user = Github(token).get_user(username)
    repo = user.get_repo(reponame)
    content = repo.get_contents(filepath)
    file_dict = {}
    if type == "file":
        return content.content
    elif type == "dir":
        for in_content in content:
            file_dict[in_content.name] = in_content.type
        return file_dict


def getPullrequet(usrtoken: str, reponame: str) -> dict:
    repo = Github(usrtoken).get_repo(reponame)
    msg = []
    for event in repo.get_events():
        if event.type == "PullRequestEvent":
            actor = event.actor.login
            time = methods.utc2cst(datetime.strftime(
                event.created_at, '%Y-%m-%dT%H:%M:%SZ'))
            msg.append({"actor": actor, "time": time})
    return msg


def getCollaborator(usrtoken: str, reponame: str):
    repo = Github(usrtoken).get_repo(reponame)
    msg = []
    for co in repo.get_collaborators():
        msg.append({"name": co.login, "avatar": co.avatar_url})
    return msg


def getrepodetail(usrtoken: str, reponame: str):
    repo = Github(usrtoken).get_repo(reponame)
    msg = {"full_name": reponame, "language": repo.language, "star": repo.stargazers_count,
           "avatar_url": repo.owner.avatar_url, "create_time": repo.created_at,
           "subscribers_count": repo.subscribers_count, "default_branch": repo.default_branch}
    return msg


def getreporeadme(usrtoken: str, reponame: str):
    repo = Github(usrtoken).get_repo(reponame)
    return repo.get_readme().content


if __name__ == '__main__':
    # print(getRepoContentDetail("Luoky76", "GCat", "backEnd/data", "dir", "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"))
    print(Github("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").get_user().id)
    pass