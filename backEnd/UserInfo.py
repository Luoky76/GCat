from click.globals import push_context
import requests
from methods import *


def getActionList(userID: str, earlyTime: float) -> list:
    """获取用户最近操作&时间列表``[(事件类型，发生时间),...]``
        :param userID:用户名
        :param earlyTime:查找时间起点
        :return:返回一个列表
    """
    data = requests.get("https://api.github.com/users/" +
                        userID+"/events").json()
    earlyTime = stemp2str(earlyTime)
    actionlist = []
    for action in data:
        if earlyTime <= action["created_at"]: 
            actionmsg = (action["type"], utc2chn(action["created_at"]))
            actionlist.append(actionmsg)

    return actionlist


if __name__ == "__main__":
    print(getActionList('QiuZeyuan',datetime.timestamp(datetime.strptime("2021-11-12T12:15:28Z", '%Y-%m-%dT%H:%M:%SZ'))))
    pass