class GEvent():

    def __init__(self, Dict: dict) -> None:
        if "token" in Dict:
            self.token = str(Dict["token"])
        if "eventID" in Dict:
            self.eventid = int(Dict["eventID"])
        if "eType" in Dict:
            self.etype = str(Dict["eType"])
        if "eTime" in Dict:
            self.etime = float(Dict["eTime"])
        if "eDetail" in Dict:
            self.edetail = dict(Dict["eDetail"])

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
