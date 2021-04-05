"""
Game Dice in Python
Robert Sharp

Outline
- Python import statements
- Random Library
- Writing Functions
"""
import random


def d(sides: int) -> int:
    """ Simple game dice. Rolls one die of any size.

    @param sides: The size of the dice to be rolled.
    @return: Random number between 1 and the number of sides.
    """
    return random.randint(1, sides)


def dice(rolls: int, sides: int) -> int:
    """ Rolls multiple dice of the same size. Returns the total.

    @param rolls: The number dice to be rolled.
    @param sides: The size of the dice to be rolled.
    @return: Random number between the number of rolls and sides times rolls.
    """
    # total = 0
    # for _ in range(rolls):
    #     total += d(sides)
    # return total
    return sum(d(sides) for _ in range(rolls))


if __name__ == '__main__':
    # This block only runs when this file is ran as a script, not when imported.
    print(d(10))
