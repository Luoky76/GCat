class GEvent(dict):
    """"
    eventID=int
    userID=str
    repoID=str
    eType=str
    eDtail=None
    eTime=float
    
    def __init__(self,Dict:dict) -> None:
        self.eventID=Dict["eventID"]
        self.eventType=Dict["eventType"]
        self.eventTime=Dict["eventTime"]
        self.userID=Dict["userID"]
        self.
        pass
    """
    def __getattr__(self, key):
            value = self.get(key)
            return GEvent(value) if isinstance(value,dict) else value
    def __setattr__(self, key, value):
            self[key] = value