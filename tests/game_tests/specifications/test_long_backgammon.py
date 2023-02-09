from ....src.game.specifications.long_backgammon import LongBackgammon
from ....src.game.game_entities.board import Board
from ....src.game.game_entities.dice import DiceRoll
from ....src.game.agent.agent import Player, PlayerColor
from ....src.game.specifications.boards_configs import LongBackgammonBoardConfig


def test_init():
    board = Board(LongBackgammonBoardConfig)
    white_agent = Player(PlayerColor.WHITE)
    black_agent = Player(PlayerColor.BLACK)

    rules = LongBackgammon()
    dice = DiceRoll(3, 4)
    available_moves = rules.get_available_moves(dice=dice, board=board, current_agent=white_agent)

    print(available_moves)


