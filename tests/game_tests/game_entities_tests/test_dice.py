from ....src.game.game_entities.dice import DiceRoll


def test_roll():
    new_dices = DiceRoll.roll()
    assert isinstance(new_dices, DiceRoll)


def test_double_init():
    new_dices = DiceRoll(1, 1)
    assert new_dices.is_double is True

    count = 0
    for dice in new_dices:
        count += 1
        assert dice == 1
    assert count == 4


def test_iter():
    new_dices = DiceRoll(1, 4)
    test_array = []
    for dice in new_dices:
        test_array.append(dice)

    assert test_array[0] == 1
    assert test_array[1] == 4


def test_reverse():
    new_dices = DiceRoll(1, 1)
    new_dices.reverse()

    for dice in new_dices:
        assert dice == -1


def test_permutations():
    new_dices = DiceRoll(1, 1)
    assert new_dices.get_permutations() == [[1, 1, 1, 1]]

    new_dices = DiceRoll(1, 2)
    assert new_dices.get_permutations() == [[1, 2], [2, 1]]