from .specification import Specification
from ..game_entities.move import Move
from ..game_entities.board import Board
from ..game_entities.cell import CellStatus
from ..agent.agent import Player, PlayerColor


class LongBackgammon(Specification):
    CHECKERS_COUNT = 15

    def check_possible_move(self, from_pos: int, to_pos: int, board: Board, current_agent: Player, base_board: Board) -> bool:
        if to_pos >= board.board_size:
            if current_agent == PlayerColor.BLACK:
                to_pos = to_pos % board.board_size
            else:
                return self.is_off_possible(current_agent, board)

        if (current_agent == PlayerColor.BLACK
                and from_pos in board.players_homes[PlayerColor.BLACK]
                and to_pos >= board.players_homes[PlayerColor][-1]
                and self.is_off_possible(current_agent, board)):
            return True

        # TODO: написать правило снятия с головы одной шашки

        # TODO: написать правило барьера из 6 шашек подряд, если впереди нет шашки противника

        if board[to_pos].status == CellStatus.FREE or board[to_pos].player == current_agent.color:
            return True

        return False

    def is_head_possible(self, actual_board: Board, base_board: Board):
        pass

    def is_off_possible(self, current_agent, board) -> bool:
        return board.get_checkers_at_home(current_agent) + board.get_checkers_at_off(current_agent) == self.CHECKERS_COUNT

    def implement_move(self, move: Move, board) -> None:
        pass

    def cancel_move(self, move: Move, board) -> None:
        pass
