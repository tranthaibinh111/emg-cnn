from enum import Enum


class EMGPosition(Enum):
    R_BIC: str = "Right Bicep"
    R_TRI: str = "Right Tricep"
    L_BIC: str = "Left Bicep"
    L_TRI: str = "Left Tricep"
    R_THI: str = "Right Thigh"
    R_HAM: str = "Right Hamstring"
    L_THI: str = "Left Thigh"
    L_HAM: str = "Left Hamstring"

    @staticmethod
    def list():
        return list(map(lambda p: p.value, EMGPosition))
    # end list()
# end class EMGPosition
