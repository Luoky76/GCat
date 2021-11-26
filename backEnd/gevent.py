class GEvent():

    def __init__(self, Dict: dict) -> None:
        self.eventid = int(Dict["eventID"])
        self.userid = str(Dict["userID"])
        self.repoid = str(Dict["repoID"])
        self.token = str(Dict["token"])
        self.etype = str(Dict["eType"])
<<<<<<< HEAD
        self.etime = float(Dict["eTime"])
        self.edetail = dict(Dict["edetail"])
=======
        self.edetail = dict(Dict["eDetail"])
        self.etime = float(Dict["eTime"])
>>>>>>> b8ebabae108a23f3b57e1fc893d447860447c7b9

    def toJson(self) -> dict:
        """ 将获得GEvent类的dict形式"""
        js = {
            "eventID": self.eventid,
            "userID": self.userid,
            "repoID": self.repoid,
            "eType": self.etype,
            "eDetail": self.edetail,
            "eTime": self.etime
        }
        return js
