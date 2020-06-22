from typing import List


class EMGModel:
    __position: str
    __data: List[float]

    def __init__(self, position: str):
        self.__position = position
        self.__data = list()
    # end __init__()

    @property
    def position(self) -> str:
        return self.__position
    # end position()

    @property
    def data(self) -> List[float]:
        return self.__data
    # end data()

    def add_data(self, value: float):
        self.__data.append(value)
    # end add_data()
# end class EMGModel
