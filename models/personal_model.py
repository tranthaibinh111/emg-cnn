from typing import List

from .action_model import ActionModel


class PersonalModel:
    __name: str
    __action: List[ActionModel]

    def __init__(self, name: str):
        self.__name = name
        self.__action = list()

    @property
    def name(self) -> str:
        return self.__name

    @property
    def action(self):
        return self.__action

    @property
    def action(self, value: List[ActionModel]):
        self.__action = self.__action + value

    def add_action(self, value: ActionModel):
        self.__action.append(value)
