"""The even game."""

from random import randint


def even_game():
    """Define even game logic."""
    question_even = randint(0, 9999)  # noqa:WPS432, S311
    if question_even % 2 == 0:
        return ['yes', question_even]
    return ['no', question_even]
