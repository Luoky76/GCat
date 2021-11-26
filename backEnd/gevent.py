class GEvent():

    def __init__(self, Dict: dict) -> None:
        self.eventid = int(Dict["eventID"])
        self.userid = str(Dict["userID"])
        self.repoid = str(Dict["repoID"])
        self.token = str(Dict["token"])
        self.etype = str(Dict["eType"])
        self.etime = float(Dict["eTime"])
        self.edetail = dict(Dict["edetail"])

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
