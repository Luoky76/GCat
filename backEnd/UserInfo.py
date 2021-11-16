import requests
import time


def getActionList(userID: str, earlyTime: float) -> list:
    """获取用户最近操作&时间列表``[[事件类型，发生时间],...]``
        :param userID:用户名
        :param earlyTime:查找时间起点
        :return:返回一个列表
    """
    data = requests.get("https://api.github.com/users/" +
                        userID+"/events").json()
    
    actionlist = []
    for action in data:
        if earlyTime <= time.mktime(time.strptime(action["created_at"], '%Y-%m-%dT%H:%M:%SZ')):

            actionmsg = [action["type"], action["created_at"]]
            actionlist.append(actionmsg)

    return actionlist


if __name__ == "__main__":
    t = time.mktime(time.strptime(
        '2021-11-12T12:31:31Z', '%Y-%m-%dT%H:%M:%SZ'))
    print(getActionList('QiuZeyuan', t))
