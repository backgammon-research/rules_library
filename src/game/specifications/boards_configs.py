from ..game_entities.cell import Cell
from ..agent.agent import PlayerColor
from dataclasses import dataclass


@dataclass()
class BaseBoardConfig:
    start_position: dict[int, Cell]
    black_home: list[int]
    white_home: list[int]


class ShortBackgammonBoardConfig(BaseBoardConfig):
    start_position = {
        0: Cell(0, PlayerColor.WHITE, 2),
        5: Cell(5, PlayerColor.BLACK, 5),
        7: Cell(7, PlayerColor.BLACK, 3),
        11: Cell(11, PlayerColor.WHITE, 5),
        12: Cell(12, PlayerColor.BLACK, 5),
        16: Cell(16, PlayerColor.WHITE, 3),
        18: Cell(18, PlayerColor.WHITE, 5),
        23: Cell(23, PlayerColor.BLACK, 2)
    }


class LongBackgammonBoardConfig(BaseBoardConfig):
    start_position = {
        0:  Cell(0, PlayerColor.WHITE, 15),
        12: Cell(12, PlayerColor.BLACK, 15)
    }

    black_home = list(range(6, 12))
    white_home = list(range(18, 24))
