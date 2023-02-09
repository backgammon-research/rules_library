from typing import Type

from .cell import Cell
from ..agent.agent import Player, PlayerColor
from ..specifications.boards_configs import BaseBoardConfig

BOARD_SIZE = 24
RENDER_CHAR = {PlayerColor.BLACK: 'X', PlayerColor.WHITE: 'O'}


class Board:
    def __init__(self, config: Type[BaseBoardConfig]):
        self.__board_size: int = BOARD_SIZE
        self.__storage = [Cell(pos) for pos in range(self.__board_size)]
        self.__checkers_off: dict[PlayerColor, int] = {PlayerColor.WHITE: 0, PlayerColor.BLACK: 0}
        self.__checkers_bar: dict[PlayerColor, int] = {PlayerColor.WHITE: 0, PlayerColor.BLACK: 0}
        self.__players_homes: dict[PlayerColor, list[int]] = {}

        self.set_configuration(config)

    @property
    def players_homes(self):
        return self.__players_homes

    @property
    def board_size(self) -> int:
        return self.__board_size

    def __getitem__(self, key: int) -> Cell:
        return self.__storage[key]

    def __setitem__(self, key: int, value: Cell) -> None:
        self.__storage[key] = value

    def __iter__(self):
        for cell in self.__storage:
            yield cell

    def implement_move(self):
        raise NotImplementedError

    def get_checkers_at_home(self, player_color: PlayerColor) -> int:
        player_checkers_at_home: int = 0
        for cell_idx in self.__players_homes[player_color]:
            cell: Cell = self[cell_idx]
            if cell.player == player_color:
                player_checkers_at_home += cell.checkers_count

        return player_checkers_at_home

    def get_checkers_at_off(self, player_color: PlayerColor) -> int:
        return self.__checkers_off[player_color]

    def set_configuration(self, config: Type[BaseBoardConfig]) -> None:
        for pos in config.start_position:
            self.__storage[pos] = config.start_position[pos]

        self.__players_homes[PlayerColor.WHITE] = config.white_home
        self.__players_homes[PlayerColor.BLACK] = config.black_home

    def render(self):
        print("| 11 | 10 |  9 |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |  0 | OFF |") # noqa
        print(f"|--------Home Black-----------|-------P={RENDER_CHAR[PlayerColor.WHITE]} Outer White-------|     |") # noqa

        for j in range(1, 16):
            row = [RENDER_CHAR[self[i].player] if self[i].checkers_count >= j else " " for i in range(11, -1, -1)] # noqa
            off = [f"{RENDER_CHAR[PlayerColor.WHITE]} " if self.__checkers_off[PlayerColor.WHITE] > j else "  "] # noqa
            row += off
            print("|  " + " |  ".join(row) + " |")

        print("|–––––––––––––––––––––––––––––|–––––––––––––––––––––––––––––|     |") # noqa

        for j in range(15, 0, -1):
            row = [RENDER_CHAR[self[i].player] if self[i].checkers_count >= j else " " for i in range(12, 24)] # noqa
            off = [f"{RENDER_CHAR[PlayerColor.BLACK]} " if self.__checkers_off[PlayerColor.BLACK] >= j else "  "] # noqa
            row += off
            print("|  " + " |  ".join(row) + " |")

        print(f"|--------P={RENDER_CHAR[PlayerColor.BLACK]} Outer Black------|------------Home White-------|     |") # noqa
        print("| 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | OFF |\n") # noqa
