class GEvent():
    
    def __init__(self,Dict:dict):
        self.eventID=int(Dict["eventID"])
        self.eType=str(Dict["eType"])
        self.eTime=float(Dict["eTime"])
        self.userID=str(Dict["userID"])
        self.eDetail=dict(Dict["eDetail"])
    
    """
    def __getattr__(self, key):
            value = self.get(key)
            return GEvent(value) if isinstance(value,dict) else value
    def __setattr__(self, key, value):
            self[key] = value
    """
