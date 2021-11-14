import requests
from requests.exceptions import RequestsWarning


def getStar(userID):
    data = requests.get('https://api.github.com/users/' +
                        userID+'/starred').json()
    starred_repos = []
    for repo in data:
        starred_repos.append(repo['full_name'])
    return starred_repos

def getRepository(userID):
    data = requests.get('https://api.github.com/users/' +
                        userID+'/repos').json()
    starred_repos = []
    for repo in data:
        starred_repos.append(repo['full_name'])
    return starred_repos

def getActionList(userID, earlyTime):

    return


def getFollowing(userID):
    data = requests.get('https://api.github.com/users/' +
                        userID + '/followers')
    for user in data:
        

    return


if __name__ == '__main__':
    print(getStar('QiuZeyuan'))
    print(getRepository('QiuZeyuan'))
