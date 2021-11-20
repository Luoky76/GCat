class GEvent():

    def __init__(self, Dict: dict) -> None:
        self.token = str(Dict["token"])
        self.eventID = int(Dict["eventID"])
        self.eType = str(Dict["eType"])
        self.eTime = float(Dict["eTime"])
        self.userID = str(Dict["userID"])
        self.eDetail = dict(Dict["eDetail"])

    def toJson(self):
        js = {
            "eventID": self.eventID,
            "eType": self.eType,
            "eTime": self.eTime,
            "userID": self.userID,
            "eDetail": self.eDetail
        }
        return js
