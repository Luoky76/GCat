class GEvent():

    def __init__(self, Dict: dict) -> None:
        self.token = str(Dict["token"])
        self.eventid = int(Dict["eventID"])
        self.etype = str(Dict["eType"])
        self.etime = float(Dict["eTime"])
        self.edetail = dict(Dict["eDetail"])

    def toJson(self) -> dict:
        """ 将获得GEvent类的dict形式"""
        js = {
            "eventID": self.eventid,
            "eType": self.etype,
            "eTime": self.etime,
            "eDetail": self.edetail
        }
        return js
