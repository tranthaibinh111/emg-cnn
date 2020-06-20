import numpy as np

from typing import List

from .emg_model import EMGModel


class ActionModel:
    __name: str
    __emg_list: List[EMGModel]

    def __init__(self, name: str, emg_list: List[EMGModel]):
        self.__name = name
        self.__emg_list = emg_list

    @property
    def name(self) -> str:
        return self.__name

    @property
    def emg_list(self) -> List[EMGModel]:
        return self.__emg_list
