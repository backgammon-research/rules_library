import pytest

from ....src.game.game_entities.cell import Cell, ExceptionCellOccupied, \
    ExceptionCellCheckersCount


def test_occupied():
    new_cell = Cell(1)
    new_cell.player = 1

    with pytest.raises(ExceptionCellOccupied):
        new_cell.player = 2


def test_add_checkers():
    new_cell = Cell(1)
    new_cell.add_checker(1)

    assert new_cell.checkers_count == 1
    assert new_cell.player == 1

    new_cell = Cell(1, 1, 15)
    with pytest.raises(ExceptionCellCheckersCount):
        new_cell.add_checker(1)


def test_remove_checkers():
    new_cell = Cell(1, 1, 1)
    new_cell.remove_checker()

    assert new_cell.checkers_count == 0
    with pytest.raises(ExceptionCellCheckersCount):
        new_cell.remove_checker()
