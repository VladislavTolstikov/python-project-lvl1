"""The even game."""

from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    """Define even game logic."""
    question = randint(1, 100)
    if question % 2 == 0:
        answer = 'yes'
        return (answer, question)
    answer = 'no'
    return (answer, question)
