import numpy as np

from typing import List

from .emg_model import EMGModel


class ActionModel:
    __name: str
    __emg_data: List[EMGModel]

    def __init__(self, name: str, emg_data: List[EMGModel]):
        self.__name = name
        self.__emg_data = emg_data
    # end __init__()

    @property
    def name(self) -> str:
        return self.__name
    # end name()

    @property
    def emg_data(self) -> List[EMGModel]:
        return self.__emg_data
    # end emg_list()
# end class ActionModel
