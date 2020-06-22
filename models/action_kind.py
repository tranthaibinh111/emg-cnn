from typing import List


class ActionKind:
    BOWING: str = "Bowing"
    CLAPPING: str = "Clapping"
    HANDSHAKING: str = "Handshaking"
    HUGGING: str = "Hugging"
    JUMPING: str = "Jumping"
    RUNNING: str = "Running"
    SEATING: str = "Seating"
    STANDING: str = "Standing"
    WALKING: str = "Walking"
    WAVING: str = "Waving"
    ELBOWING: str = "Elbowing"
    FRONTKICKING: str = "Frontkicking"
    HAMERING: str = "Hamering"
    HEADERING: str = "Headering"
    KNEEING: str = "Kneeing"
    PULLING: str = "Pulling"
    PUNCHING: str = "Punching"
    PUSHING: str = "Pushing"
    SIDEKICKING: str = "Sidekicking"
    SLAPPING: str = "Slapping"

    @staticmethod
    def get_normal_action() -> List[str]:
        return [ActionKind.BOWING, ActionKind.CLAPPING, ActionKind.HANDSHAKING, ActionKind.HUGGING, ActionKind.JUMPING,
                ActionKind.RUNNING, ActionKind.SEATING, ActionKind.STANDING, ActionKind.WALKING, ActionKind.WAVING]
    # end get_normal_action()

    @staticmethod
    def get_aggressive_action() -> List[str]:
        return [ActionKind.ELBOWING, ActionKind.FRONTKICKING, ActionKind.HAMERING, ActionKind.HEADERING,
                ActionKind.KNEEING, ActionKind.PULLING, ActionKind.PUNCHING, ActionKind.PUSHING, ActionKind.SIDEKICKING,
                ActionKind.SLAPPING]
    # end get_aggressive_action()
# end class ActionKind
