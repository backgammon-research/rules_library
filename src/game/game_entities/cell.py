"""Module to work with atomic unit of board - Cell"""

from enum import Enum
from typing import Optional
from ..agent.agent import Player, PlayerColor


class ExceptionCell(Exception):
    """Main exception class for cell"""


class ExceptionCellOccupied(ExceptionCell):
    """Raise when user try to set different players in one cell"""
    def __str__(self):
        return "Cell still occupied by another player"


class ExceptionCellCheckersCount(ExceptionCell):
    """Raise when checkers count in cell < 0 or > 15"""
    def __init__(self, actual_checkers_count):
        self.value = actual_checkers_count

    def __str__(self):
        return f"Count of checkers should be: 0 to 15. " \
               f"Actual size of checkers: {self.value}"


class CellStatus(Enum):
    """
    FREE - 0 checkers in cell
    OCCUPIED - 2 and more checkers in cell
    BLOT - 1 checker in cell
    """
    FREE = 0
    OCCUPIED = 1
    BLOT = 2


class Cell:
    """
    Atomic unit of board
    """
    def __init__(self, boarder_pos: int, player_color: Optional[PlayerColor] = None, checkers_count: int = 0): # noqa
        self.__pos: int = boarder_pos
        self.__player_color: Optional[PlayerColor] = player_color
        self.__checkers_count: int = checkers_count
        self.__status = CellStatus.FREE
        self.update_status()

    @property
    def pos(self) -> int:
        return self.__pos

    @property
    def status(self) -> CellStatus:
        return self.__status

    @property
    def player(self) -> PlayerColor:
        return self.__player_color

    @player.setter
    def player(self, player_color: Player) -> None:
        if self.__player_color is not None and self.__player_color != player_color: # noqa
            raise ExceptionCellOccupied

        self.__player_color = player_color

    @property
    def checkers_count(self) -> int:
        return self.__checkers_count

    def add_checker(self, player_color: Player) -> None:
        self.player = player_color
        self.__checkers_count += 1

        if self.__checkers_count > 15:
            raise ExceptionCellCheckersCount(self.checkers_count)

        self.update_status()

    def update_status(self):
        if self.__checkers_count == 0:
            self.__status = CellStatus.FREE
        elif self.__checkers_count == 1:
            self.__status = CellStatus.BLOT
        elif self.__checkers_count >= 2:
            self.__status = CellStatus.OCCUPIED

    def remove_checker(self) -> None:
        self.__checkers_count -= 1

        if self.checkers_count < 0:
            raise ExceptionCellCheckersCount(self.checkers_count)

        self.update_status()

    def __str__(self):
        return f"Player: {self.player}, checkers_count: {self.checkers_count}"
