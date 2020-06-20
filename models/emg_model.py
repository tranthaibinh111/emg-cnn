from typing import List


class EMGModel:
    __position: str
    __data: List[int]

    def __init__(self, position: str):
        self.__position = position
        self.__data = list()

    @property
    def position(self) -> str:
        return self.__position

    @property
    def data(self) -> List[int]:
        return self.__data

    def add_data(self, value: int):
        self.__data.append(value)
