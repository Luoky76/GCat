class GEvent():

    def __init__(self, Dict: dict) -> None:
        self.token = str(Dict["token"])
        self.eventID = int(Dict["eventID"])
        self.eType = str(Dict["eType"])
        self.eTime = float(Dict["eTime"])
        self.eDetail = dict(Dict["eDetail"])

    def toJson(self) -> dict:
        js = {
            "eventID": self.eventID,
            "eType": self.eType,
            "eTime": self.eTime,
            "eDetail": self.eDetail
        }
        return js
