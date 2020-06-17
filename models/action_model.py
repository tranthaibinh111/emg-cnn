import numpy as np

from .emg_model import EMGModel


class ActionModel:
    def __init__(self, name: str):
        self.__name = name
        self.r_bic = EMGModel(position="Right Bicep")
        self.r_tri = EMGModel(position="Right Tricep")
        self.l_bic = EMGModel(position="Left Bicep")
        self.l_tri = EMGModel(position="Left Tricep")
        self.r_thi = EMGModel(position="Right Thigh")
        self.r_ham = EMGModel(position="Right Hamstring")
        self.l_thi = EMGModel(position="Left Thigh")
        self.l_ham = EMGModel(position="Left Hamstring")

    @property
    def name(self) -> str:
        return self.__name
