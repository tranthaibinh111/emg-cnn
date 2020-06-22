from typing import List

from .action_model import ActionModel


class PersonModel:
    __name: str
    __action: List[ActionModel]

    def __init__(self, name: str):
        self.__name = name
        self.__action = list()
    # end __init__

    @property
    def name(self) -> str:
        return self.__name
    # end name()

    @property
    def action(self) -> List[ActionModel]:
        return self.__action
    # end action()

    @action.setter
    def action(self, value: List[ActionModel]):
        self.__action = self.__action + value
    # end action()

    def add_action(self, value: ActionModel):
        self.__action.append(value)
    # end add_action()
# end class PersonModel
