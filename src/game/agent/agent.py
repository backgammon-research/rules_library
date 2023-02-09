from enum import Enum


class PlayerColor(Enum):
    WHITE = 0
    BLACK = 1


class Player:
    def __init__(self, color: PlayerColor):
        self.__color = color

    @property
    def color(self):
        return self.__color

    def __eq__(self, other: PlayerColor):
        return self.__color == other
