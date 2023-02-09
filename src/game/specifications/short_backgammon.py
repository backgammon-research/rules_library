from .specification import Specification
from ..game_entities.board import Board
from ..game_entities.dice import DiceRoll
from .boards_configs import ShortBackgammonBoardConfig
from ..agent.agent import PlayerColor
from ..game_entities.move import Move


class ShortBackgammon(Specification):
    """
    Classical backgammon rules implementation
    """

    def implement_move(self, move: Move, board) -> None:
        pass

    def cancel_move(self, move: Move, board) -> None:
        pass

    def check_possible_move(self, from_pos, to_pos, board) -> bool:
        pass
