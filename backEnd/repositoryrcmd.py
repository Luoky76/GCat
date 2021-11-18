from click.globals import push_context
import requests

class Repositoryrcmd():
    def __init__(self, name):
        self.name = name
    def __get_keyword(self):#私有方法
        """获取用户的收藏仓库&高频keyword``[(事件类型，发生时间),...]``
            :param userID:用户名
            :return:返回一个keyword列表
        """
        data = requests.get("https://api.github.com/users/" + self.name + "/starred").json()
        stat_list = list();
        for each in data:
            list.append("https://raw.githubusercontent.com/"+each["fullname"]+"/master/README.md")


    def get_name(self):
        pass

if __name__ == "__main__":
    data = requests.get("https://raw.githubusercontent.com/Luoky76/GCat/master/README.md").json()
    print(data)
    pass