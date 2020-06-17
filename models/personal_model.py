from .action_model import ActionModel


class PersonalModel:
    def __init__(self, name: str):
        self.__name = name

        # region Normal Physical Actions
        self.bowing: ActionModel = None
        self.clapping: ActionModel = None
        self.handshaking: ActionModel = None
        self.hugging: ActionModel = None
        self.jumping: ActionModel = None
        self.running: ActionModel = None
        self.seating: ActionModel = None
        self.standing: ActionModel = None
        self.walking: ActionModel = None
        self.waving: ActionModel = None
        # endregion

        # region Aggressive Physical Actions
        self.elbowing: ActionModel = None
        self.frontkicking: ActionModel = None
        self.hamering: ActionModel = None
        self.headering: ActionModel = None
        self.kneeing: ActionModel = None
        self.pulling: ActionModel = None
        self.punching: ActionModel = None
        self.pushing: ActionModel = None
        self.sidekicking: ActionModel = None
        self.slapping: ActionModel = None
        # endregion

    @property
    def name(self) -> str:
        return self.__name
