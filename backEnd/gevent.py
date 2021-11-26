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
        if "edetail" in Dict:
            self.edetail = dict(Dict["edetail"])

    def toJson(self) -> dict:
        """ 将获得GEvent类的dict形式"""
        js = {
            "eventID": self.eventid,
            "eType": self.etype,
            "eTime": self.etime,
            "edetail": self.edetail
        }
        return js
