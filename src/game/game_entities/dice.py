from random import randint


class DiceRoll:
    def __init__(self, dice_1, dice_2):
        self.dice_1: int = dice_1
        self.dice_2: int = dice_2
        self.is_double = dice_1 == dice_2

    def __iter__(self) -> int:
        dices_array = [self.dice_1] * 4 if self.is_double else [self.dice_1, self.dice_2] # noqa
        for dice in dices_array:
            yield dice

    def __str__(self):
        return ' '.join([f"dice_{idx}={str(dice)}" for idx, dice in enumerate(self)]) # noqa

    def reverse(self):
        """
        Assigns negative values for dices.
        Use it when calculating moves for black color agent.
        """
        self.dice_1 = -self.dice_1
        self.dice_2 = -self.dice_2

    def get_permutations(self) -> list[list[int]]:
        return [[self.dice_1 for _ in range(4)]] if self.is_double \
            else [[self.dice_1, self.dice_2], [self.dice_2, self.dice_1]]

    @staticmethod
    def roll(first_roll=False) -> 'DiceRoll':
        """
        Get DiceRoll.
        Use 'first_roll=True' in case of first turn because of rules of all specifications
        """ # noqa
        def get_roll():
            return randint(1, 6), randint(1, 6)

        dice_1, dice_2 = get_roll()
        while first_roll and dice_1 == dice_2:
            dice_1, dice_2 = get_roll()

        return DiceRoll(dice_1, dice_2)
