from __future__ import annotations

import random


def roll_dice(count, dice, full=False):
    rolls = [random.randint(1, dice) for _ in range(count)]
    if full:
        return sum(rolls), rolls
    else:
        return sum(rolls)


class DiceRoller:
    """For persistent values for dice rolls"""
    def __init__(self, count, dice):
        self.count = count
        self.dice = dice

    def __call__(self, *args, **kwargs):
        return roll_dice(self.count, self.dice, full=kwargs.get('full', False))


def _test():
    dice5d20 = DiceRoller(5, 20)
    print(dice5d20())
    print(dice5d20())
    print(dice5d20())
    print(dice5d20())


if __name__ == '__main__':
    _test()
