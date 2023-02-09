from ....src.game.game_entities.board import Board
from ....src.game.specifications.boards_configs import LongBackgammonBoardConfig, BaseBoardConfig
from ....src.game.agent.agent import Player, PlayerColor
from ....src.game.game_entities.cell import Cell


def test_longbackgammon_config_init():
    board = Board(LongBackgammonBoardConfig)

    assert board[0].player == PlayerColor.WHITE
    assert board[0].checkers_count == 15

    assert board[12].player == PlayerColor.BLACK
    assert board[12].checkers_count == 15

    assert board.get_checkers_at_off(PlayerColor.WHITE) == 0
    assert board.get_checkers_at_off(PlayerColor.BLACK) == 0

    assert board.players_homes[PlayerColor.WHITE] == list(range(18, 24))
    assert board.players_homes[PlayerColor.BLACK] == list(range(6, 12))

    assert board.board_size == 24


def test_checkers_at_home():
    board = Board(LongBackgammonBoardConfig)
    white_player = Player(PlayerColor.WHITE)
    black_player = Player(PlayerColor.BLACK)

    assert board.get_checkers_at_home(white_player.color) == 0
    assert board.get_checkers_at_home(black_player.color) == 0

    class TestHomeCheckersConfig(BaseBoardConfig):
        start_position = {
            0: Cell(0, PlayerColor.BLACK, 1),
            1: Cell(1, PlayerColor.BLACK, 1),
            2: Cell(2, PlayerColor.WHITE, 1),
            3: Cell(3, PlayerColor.WHITE, 1)
        }

        black_home = list(range(0, 2))
        white_home = list(range(2, 4))

    board = Board(TestHomeCheckersConfig)

    assert board.get_checkers_at_home(white_player.color) == 2
    assert board.get_checkers_at_home(black_player.color) == 2

    class TestHomeCheckersConfig2(BaseBoardConfig):
        start_position = {
            0: Cell(0, PlayerColor.BLACK, 1),
            1: Cell(1, PlayerColor.BLACK, 1),
            2: Cell(2, PlayerColor.WHITE, 1),
            3: Cell(3, PlayerColor.WHITE, 1)
        }

        black_home = list(range(0, 6))
        white_home = list(range(6, 12))

    board = Board(TestHomeCheckersConfig2)

    assert board.get_checkers_at_home(white_player.color) == 0
    assert board.get_checkers_at_home(black_player.color) == 2


def test_render_work():
    board = Board(LongBackgammonBoardConfig)
    board.render()
