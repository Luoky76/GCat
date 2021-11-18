import GEvent
class AbstractEventHandler():
    def evExecute(newEvent:GEvent):
        pass
    pass

class EventDistributer(AbstractEventHandler):
    pass

class RecommendEventHandler(AbstractEventHandler):
    pass

class GetInfoEventHandler(AbstractEventHandler):
    pass

class ChangeUserInfoEventHandler(AbstractEventHandler):
    pass

class LoginEventHandler(AbstractEventHandler):
    pass

class CreateRepoEventHandler(AbstractEventHandler):
    pass

class UpdateRepoEventHandler(AbstractEventHandler):
    pass